import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from px4_msgs.msg import VehicleLocalPosition
from drone_interfaces.msg import Waypoint, WaypointArray, WaypointVisited, DroneStatusUpdate
import math
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy


class MissionHandlerNode(Node):

    def __init__(self):
        super().__init__('mission_handler_node')
        self.get_logger().info("Mission Handler Node: Initializing...")

        # QoS Profile for PX4 topics (best effort for sensor data)
        # Note: Your WaypointArray subscription doesn't use this specific QoS,
        # it uses the default, which is usually reliable.
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.get_logger().debug("Mission Handler Node: QoS profile created.")

        # Mission state variables
        self.current_waypoints = []
        self.current_index = 0
        self.active = False
        self.drone_id = 'drone_1' # Crucial: Ensure this matches the ID used by the WaypointPublisher's request!
        self.reached_threshold = 1.0  # meters
        self.current_target = None  # Waypoint currently being tracked
        self.get_logger().info(f"Mission Handler Node: Drone ID set to '{self.drone_id}'.")

        # Subscriptions
        waypoints_topic = f'/drone/{self.drone_id}/waypoints'
        self.get_logger().info(f"Mission Handler Node: Attempting to subscribe to '{waypoints_topic}' for waypoints...")
        self.create_subscription(
            WaypointArray,
            waypoints_topic,
            self.waypoint_callback,
            10 # Default QoS for this subscription (ReliabilityPolicy.RELIABLE, DurabilityPolicy.VOLATILE, HistoryPolicy.KEEP_LAST)
        )
        self.get_logger().info(f"Mission Handler Node: Subscription to '{waypoints_topic}' created.")

        self.get_logger().info("Mission Handler Node: Attempting to subscribe to '/fmu/out/vehicle_local_position'...")
        self.create_subscription(
            VehicleLocalPosition,
            '/fmu/out/vehicle_local_position',
            self.position_callback,
            qos_profile
        )
        self.get_logger().info("Mission Handler Node: Subscription to '/fmu/out/vehicle_local_position' created.")


        # Publishers
        self.setpoint_pub = self.create_publisher(PoseStamped, '/offboard_setpoint_pose', 10)
        self.get_logger().info("Mission Handler Node: Publisher for '/offboard_setpoint_pose' created.")

        self.waypoint_update_pub = self.create_publisher(WaypointVisited, '/mission_handler/waypoint_visited', 10)
        self.get_logger().info("Mission Handler Node: Publisher for '/mission_handler/waypoint_visited' created.")

        drone_status_topic = f'/{self.drone_id}/update_status'
        self.status_update_pub = self.create_publisher(DroneStatusUpdate, drone_status_topic, 10)
        self.get_logger().info(f"Mission Handler Node: Publisher for '{drone_status_topic}' created.")

        self._send_status_update("idle")
        self.get_logger().info("Mission Handler Node: Initialization complete.")

    def _send_status_update(self, status: str):
        """Publishes a drone status update."""
        msg = DroneStatusUpdate()
        msg.status = status
        self.status_update_pub.publish(msg)
        self.get_logger().info(f"Mission Handler Node [{self.drone_id}]: Published status update: '{status}'")

    def waypoint_callback(self, msg: WaypointArray):
        """Callback for receiving WaypointArray messages."""
        self.get_logger().info("Mission Handler Node: >>> WAYPOINT CALLBACK TRIGGERED <<<")
        self.get_logger().info(f"Mission Handler Node: Received WaypointArray message.")

        if not msg.waypoints:
            self.get_logger().warn("Mission Handler Node: Received empty waypoint list. Setting status to idle.")
            self._send_status_update("idle")
            self.active = False # Ensure mission is deactivated
            return

        self.get_logger().info(f"Mission Handler Node: Received {len(msg.waypoints)} waypoints. Starting mission.")
        self.current_waypoints = msg.waypoints
        self.current_index = 0
        self.active = True
        self._send_status_update("executing")
        self._publish_next_waypoint()
        self.get_logger().debug("Mission Handler Node: Waypoint callback processed.")

    def _publish_next_waypoint(self):
        """Publishes the next waypoint from the current mission to the setpoint topic."""
        self.get_logger().debug(f"Mission Handler Node: Attempting to publish next waypoint. Current index: {self.current_index}, Total waypoints: {len(self.current_waypoints)}")

        if self.current_index >= len(self.current_waypoints):
            self.get_logger().info(f"Mission Handler Node [{self.drone_id}]: All waypoints visited. Mission complete.")
            self._send_status_update("idle")
            self.active = False
            self.current_target = None
            return

        waypoint = self.current_waypoints[self.current_index]
        self.current_target = waypoint  # Save target
        self.get_logger().info(f"Mission Handler Node: Setting current target to Waypoint ID {waypoint.id} (Lat: {waypoint.lat}, Lon: {waypoint.lon}, Alt: {waypoint.alt}).")

        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = "map"  # Adjust if needed based on your coordinate frame
        pose.pose.position.x = waypoint.lat  # Assuming local coordinates
        pose.pose.position.y = waypoint.lon
        pose.pose.position.z = waypoint.alt

        self.setpoint_pub.publish(pose)
        self.get_logger().info(f"Mission Handler Node: Published waypoint ID {waypoint.id} to /offboard_setpoint_pose")

    def position_callback(self, msg: VehicleLocalPosition):
        """Callback for receiving current local position of the vehicle."""
        # This callback can be very frequent, so use debug for its internal logging
        # self.get_logger().debug(f"Mission Handler Node: Position callback received. X: {msg.x}, Y: {msg.y}, Z: {msg.z}")

        if not self.active or self.current_target is None:
            # self.get_logger().debug("Mission Handler Node: Not active or no current target. Skipping position check.")
            return

        dx = self.current_target.lat - msg.x # Assuming current_target.lat/lon are local x/y
        dy = self.current_target.lon - msg.y
        dz = self.current_target.alt - msg.z
        dist = math.sqrt(dx**2 + dy**2 + dz**2)

        # self.get_logger().debug(f"Mission Handler Node: Distance to target {self.current_target.id}: {dist:.2f}m")

        if dist <= self.reached_threshold:
            self.get_logger().info(f"Mission Handler Node: Reached waypoint ID {self.current_target.id} (within {dist:.2f}m threshold of {self.reached_threshold}m)")
            
            # Publish WaypointVisited message
            update = WaypointVisited()
            update.drone_id = self.drone_id
            update.waypoint_id = self.current_target.id
            self.waypoint_update_pub.publish(update)
            self.get_logger().info(f"Mission Handler Node: Published WaypointVisited for ID {self.current_target.id}.")

            # Move to the next waypoint
            self.current_index += 1
            self._publish_next_waypoint()
        # else:
            # self.get_logger().debug(f"Mission Handler Node: Not yet at waypoint {self.current_target.id}. Distance: {dist:.2f}m")


def main(args=None):
    rclpy.init(args=args)
    node = MissionHandlerNode()
    node.get_logger().info("Mission Handler Node: Starting spin loop...")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Mission Handler Node: KeyboardInterrupt received. Shutting down.")
    finally:
        node.destroy_node()
        rclpy.shutdown()
        node.get_logger().info("Mission Handler Node: Node destroyed and rclpy shut down.")


if __name__ == '__main__':
    main()