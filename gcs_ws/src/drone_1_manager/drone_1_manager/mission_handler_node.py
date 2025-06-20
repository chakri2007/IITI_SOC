import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from px4_msgs.msg import VehicleLocalPosition
from drone_interfaces.msg import Waypoint, WaypointArray, WaypointVisited, DroneStatusUpdate
from drone_interfaces.msg import Geotag, GeotagArray
import math
import time
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from pyproj import Proj, transform


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

        self.drone_id = 'drone_1'
        self.drone_type = 'surveillance'
        self.drone_status = 'executing'
        self.current_waypoints = []
        self.severity_scores = {}  # Map: waypoint_id -> severity_score
        self.current_index = 0
        self.active = False
        self.reached_threshold = 1.0  # meters
        self.current_target = None
        self.waiting_until = None

        self.origin_set = False
        self.origin_lat = None
        self.origin_lon = None
        self.origin_alt = None
        self.geodetic_proj = Proj(proj='latlong', datum='WGS84')
        self.enu_proj = None

        self.create_subscription(DroneStatusUpdate, f'/{self.drone_id}/status', self.status_callback, 10)
        self.create_subscription(VehicleLocalPosition, '/fmu/out/vehicle_local_position', self.position_callback, qos_profile)

        self.setpoint_pub = self.create_publisher(PoseStamped, '/offboard_setpoint_pose', 10)
        self.waypoint_update_pub = self.create_publisher(WaypointVisited, '/mission_handler/waypoint_visited', 10)
        self.status_update_pub = self.create_publisher(DroneStatusUpdate, f'/{self.drone_id}/update_status', 10)

        self._send_status_update("idle")
        self.get_logger().info("Mission Handler Node: Initialization complete.")

    def status_callback(self, msg: DroneStatusUpdate):
        if msg.drone_id != self.drone_id:
            return

        self.drone_type = msg.type
        self.drone_status = msg.status

        if self.drone_type == 'irrigation':
            topic = '/geotag_array'
            self.create_subscription(GeotagArray, topic, self.geotag_callback, 10)
        else:
            topic = f'/drone/{self.drone_id}/waypoints'
            self.create_subscription(WaypointArray, topic, self.waypoint_callback, 10)

        self.get_logger().info(f"Subscribed to: {topic} based on type '{self.drone_type}'")

    def _send_status_update(self, status: str):
        msg = DroneStatusUpdate()
        msg.status = status
        msg.drone_id = self.drone_id
        self.status_update_pub.publish(msg)
        self.get_logger().info(f"Status update: '{status}'")

    def waypoint_callback(self, msg: WaypointArray):
        self.get_logger().info(">>> WAYPOINT CALLBACK TRIGGERED <<<")

        if not msg.waypoints:
            self.get_logger().warn("Received empty waypoint list. Setting status to idle.")
            self._send_status_update("idle")
            self.active = False
            return

        self.get_logger().info(f"Received {len(msg.waypoints)} waypoints. Starting mission.")
        self.current_waypoints = msg.waypoints
        self.severity_scores.clear()  # Not used for surveillance
        self.current_index = 0
        self.active = True
        self._send_status_update("executing")
        self._publish_next_waypoint()

    def geotag_callback(self, msg: GeotagArray):
        self.get_logger().info(">>> GEOTAG CALLBACK TRIGGERED <<<")

        if not msg.geotags:
            self.get_logger().warn("Received empty geotag list. Setting status to idle.")
            self._send_status_update("idle")
            self.active = False
            return

        self.get_logger().info(f"Received {len(msg.geotags)} geotags. Converting to waypoints.")
        self.current_waypoints = []
        self.severity_scores = {}

        for geotag in msg.geotags:
            waypoint = Waypoint()
            waypoint.id = int(geotag.id)
            waypoint.lat = geotag.lat
            waypoint.lon = geotag.lon
            waypoint.alt = geotag.alt
            waypoint.visited = False
            self.current_waypoints.append(waypoint)
            self.severity_scores[waypoint.id] = geotag.severity_score

        self.current_index = 0
        self.active = True
        self._send_status_update("executing")
        self._publish_next_waypoint()

    def _publish_next_waypoint(self):
        if self.drone_status not in ['idle', 'executing']:
            self.get_logger().info("Drone status not idle or executing. Skipping waypoint publish.")
            return

        if self.current_index >= len(self.current_waypoints):
            self.get_logger().info("All waypoints visited. Mission complete.")
            self._send_status_update("idle")
            self.active = False
            self.current_target = None
            return

        waypoint = self.current_waypoints[self.current_index]
        self.current_target = waypoint

        if not self.origin_set:
            self.get_logger().warn("Origin not yet set. Waiting for position data.")
            return

        try:
            x_east, y_north = transform(
                self.geodetic_proj,
                self.enu_proj,
                waypoint.lon,
                waypoint.lat
            )
            z_down = -(waypoint.alt - self.origin_alt)

            pose = PoseStamped()
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.header.frame_id = "map"
            pose.pose.position.x = y_north
            pose.pose.position.y = x_east
            pose.pose.position.z = z_down

            self.setpoint_pub.publish(pose)

            self.get_logger().info(
                f"Published waypoint ID {waypoint.id} to /offboard_setpoint_pose "
                f"(N: {y_north:.2f}, E: {x_east:.2f}, D: {z_down:.2f})"
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
            self.get_logger().info(f"Origin set at (Lat: {self.origin_lat}, Lon: {self.origin_lon}, Alt: {self.origin_alt})")

        if not self.active or self.current_target is None or not self.origin_set:
            return

        dx = self.current_target.lat - msg.x
        dy = self.current_target.lon - msg.y
        dz = self.current_target.alt - msg.z
        dist = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

        if dist <= self.reached_threshold:
            if self.waiting_until is None:
                self.get_logger().info(f"Reached waypoint ID {self.current_target.id} (Distance: {dist:.2f}m)")

                if self.drone_type == 'irrigation':
                    score = self.severity_scores.get(self.current_target.id, 1)
                    wait_time = score * 10
                    self.waiting_until = time.time() + wait_time
                    self.get_logger().info(f"Waiting {wait_time} seconds at waypoint due to severity score {score}")
                else:
                    self.waiting_until = time.time()  # no wait for surveillance
            elif time.time() >= self.waiting_until:
                update = WaypointVisited()
                update.drone_id = self.drone_id
                update.waypoint_id = self.current_target.id
                self.waypoint_update_pub.publish(update)

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
