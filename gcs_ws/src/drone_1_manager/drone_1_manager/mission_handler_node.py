import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from px4_msgs.msg import VehicleLocalPosition
from drone_interfaces.msg import Waypoint, WaypointArray, WaypointVisited, DroneStatus, DroneStatusUpdate, Geotag, GeotagArray
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from pyproj import Proj, transform
import math

class MissionHandlerNode(Node):

    def __init__(self):
        super().__init__('mission_handler_node')
        self.get_logger().info("Mission Handler Node: Initializing...")

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # State
        self.drone_id = 'drone_1'
        self.drone_type = None
        self.current_waypoints = []
        self.severity_scores = {}  # waypoint_id -> severity
        self.current_index = 0
        self.active = False
        self.reached_threshold = 1.0  # meters
        self.current_target = None
        self.target_local_pos = None
        self.waiting_until = None
        self.origin_set = False
        self.origin_lat = None
        self.origin_lon = None
        self.origin_alt = None
        self.geodetic_proj = Proj(proj='latlong', datum='WGS84')
        self.enu_proj = None

        # Flags
        self.subscribed_to_geotag = False
        self.subscribed_to_waypoints = False

        # Subscriptions
        self.create_subscription(DroneStatus, f'/{self.drone_id}/status', self.status_callback, 10)
        self.create_subscription(VehicleLocalPosition, '/px4_1/fmu/out/vehicle_local_position', self.position_callback, qos_profile)

        # Publishers
        self.setpoint_pub = self.create_publisher(PoseStamped, '/drone_1/offboard_setpoint_pose', 10)
        self.waypoint_update_pub = self.create_publisher(WaypointVisited, '/mission_handler/waypoint_visited', 10)
        self.status_update_pub = self.create_publisher(DroneStatusUpdate, f'/{self.drone_id}/update_status', 10)

        self._send_status_update("idle")
        self.get_logger().info("Mission Handler Node: Initialization complete.")

    def _send_status_update(self, status: str):
        msg = DroneStatusUpdate()
        msg.status = status
        msg.drone_id = self.drone_id
        self.status_update_pub.publish(msg)
        self.get_logger().info(f"Status update: '{status}'")

    def status_callback(self, msg: DroneStatus):
        if msg.drone_id != self.drone_id:
            return

        if msg.type != self.drone_type:
            self.drone_type = msg.type
            self.get_logger().info(f"Drone type set to: {self.drone_type}")

            if self.drone_type == 'irrigation' and not self.subscribed_to_geotag:
                self.create_subscription(GeotagArray, '/drone_1/geotag_array', self.geotag_callback, 10)
                self.subscribed_to_geotag = True
                self.get_logger().info("Subscribed to /drone_1/geotag_array")
            elif self.drone_type == 'surveillance' and not self.subscribed_to_waypoints:
                self.create_subscription(WaypointArray, f'/drone/{self.drone_id}/waypoints', self.waypoint_callback, 10)
                self.subscribed_to_waypoints = True
                self.get_logger().info(f"Subscribed to /drone/{self.drone_id}/waypoints")

    def waypoint_callback(self, msg: WaypointArray):
        self.get_logger().info(">>> WAYPOINT CALLBACK <<<")
        if not msg.waypoints:
            self.get_logger().warn("Received empty waypoint list.")
            self._send_status_update("idle")
            self.active = False
            return

        self.current_waypoints = msg.waypoints
        self.severity_scores.clear()
        self.current_index = 0
        self.active = True
        self._send_status_update("executing")
        self._publish_next_waypoint()

    def geotag_callback(self, msg: GeotagArray):
        self.get_logger().info(">>> GEOTAG CALLBACK <<<")
        if not msg.geotags:
            self.get_logger().warn("Received empty geotag list.")
            self._send_status_update("idle")
            self.active = False
            return

        self.current_waypoints = []
        self.severity_scores = {}

        for geotag in msg.geotags:
            wp = Waypoint()
            wp.id = int(geotag.id)
            wp.lat = geotag.lat
            wp.lon = geotag.lon
            wp.alt = geotag.alt
            wp.visited = False
            self.current_waypoints.append(wp)
            self.severity_scores[wp.id] = geotag.severity_score

        self.current_index = 0
        self.active = True
        self._send_status_update("executing")
        self._publish_next_waypoint()

    def _publish_next_waypoint(self):
        if self.current_index >= len(self.current_waypoints):
            self.get_logger().info("All waypoints visited. Mission complete.")
            self._send_status_update("idle")
            self.active = False
            self.current_target = None
            self.target_local_pos = None
            return

        if not self.origin_set:
            self.get_logger().warn("Origin not yet set. Waiting for position data.")
            return

        wp = self.current_waypoints[self.current_index]
        self.current_target = wp

        try:
            x_east, y_north = transform(self.geodetic_proj, self.enu_proj, wp.lon, wp.lat)
            z_down = -(wp.alt - self.origin_alt)

            # Save for distance check
            self.target_local_pos = (y_north, x_east, z_down)

            pose = PoseStamped()
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.header.frame_id = "map"
            pose.pose.position.x = y_north
            pose.pose.position.y = x_east
            pose.pose.position.z = z_down

            self.setpoint_pub.publish(pose)
            self.get_logger().info(
                f"Published waypoint ID {wp.id} → (N: {y_north:.2f}, E: {x_east:.2f}, D: {z_down:.2f})"
            )
        except Exception as e:
            self.get_logger().error(f"Failed to convert GPS to NED: {str(e)}")

    def position_callback(self, msg: VehicleLocalPosition):
        if not self.origin_set and msg.ref_lat != 0.0 and msg.ref_lon != 0.0:
            self.origin_lat = msg.ref_lat
            self.origin_lon = msg.ref_lon
            self.origin_alt = msg.ref_alt
            self.enu_proj = Proj(proj='aeqd', lat_0=self.origin_lat, lon_0=self.origin_lon, datum='WGS84')
            self.origin_set = True
            self.get_logger().info(
                f"Origin set at (Lat: {self.origin_lat}, Lon: {self.origin_lon}, Alt: {self.origin_alt})"
            )

        if not self.active or self.current_target is None or not self.origin_set or self.target_local_pos is None:
            return

        dx = self.target_local_pos[0] - msg.x
        dy = self.target_local_pos[1] - msg.y
        dz = self.target_local_pos[2] - msg.z
        dist = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

        if dist <= self.reached_threshold:
            now = self.get_clock().now().nanoseconds
            if self.waiting_until is None:
                self.get_logger().info(f"Reached waypoint ID {self.current_target.id} (Distance: {dist:.2f}m)")

                if self.drone_type == 'irrigation':
                    severity = self.severity_scores.get(self.current_target.id, 1)
                    wait_time_sec = severity * 10
                    self.waiting_until = now + int(wait_time_sec * 1e9)
                    self.get_logger().info(f"Waiting {wait_time_sec} seconds at waypoint due to severity {severity}")
                else:
                    self.waiting_until = now  # No wait
            elif now >= self.waiting_until:
                visited = WaypointVisited()
                visited.drone_id = self.drone_id
                visited.waypoint_id = self.current_target.id
                self.waypoint_update_pub.publish(visited)

                self.waiting_until = None
                self.current_index += 1
                self._publish_next_waypoint()


def main(args=None):
    rclpy.init(args=args)
    node = MissionHandlerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("KeyboardInterrupt received. Shutting down.")
    finally:
        node.destroy_node()
        rclpy.shutdown()
        node.get_logger().info("Node destroyed and rclpy shut down.")


if __name__ == '__main__':
    main()