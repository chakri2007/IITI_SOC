import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from px4_msgs.msg import VehicleLocalPosition
from drone_interfaces.msg import Waypoint, WaypointArray, WaypointVisited, DroneStatusUpdate
import math


class MissionHandlerNode(Node):

    def __init__(self):
        super().__init__('mission_handler_node')
        self.get_logger().info("Mission Handler Node Started.")

        self.current_waypoints = []
        self.current_index = 0
        self.active = False
        self.drone_id = 'drone_1'
        self.reached_threshold = 1.0  # meters

        self.current_target = None  # Waypoint currently being tracked

        self.create_subscription(WaypointArray, f'/drone/{self.drone_id}/waypoints', self.waypoint_callback, 10)
        self.create_subscription(VehicleLocalPosition, '/fmu/out/vehicle_local_position', self.position_callback, 10)

        self.setpoint_pub = self.create_publisher(PoseStamped, '/offboard_setpoint_pose', 10)
        self.waypoint_update_pub = self.create_publisher(WaypointVisited, '/mission_handler/waypoint_visited', 10)
        self.status_update_pub = self.create_publisher(DroneStatusUpdate, f'/{self.drone_id}/update_status', 10)

        self._send_status_update("idle")

    def _send_status_update(self, status: str):
        msg = DroneStatusUpdate()
        msg.status = status
        self.status_update_pub.publish(msg)
        self.get_logger().info(f"[{self.drone_id}] Published status update: {status}")

    def waypoint_callback(self, msg: WaypointArray):
        if not msg.waypoints:
            self.get_logger().warn("Received empty waypoint list.")
            self._send_status_update("idle")
            return

        self.get_logger().info(f"Received {len(msg.waypoints)} waypoints. Starting mission.")
        self.current_waypoints = msg.waypoints
        self.current_index = 0
        self.active = True
        self._send_status_update("executing")
        self._publish_next_waypoint()

    def _publish_next_waypoint(self):
        if self.current_index >= len(self.current_waypoints):
            self.get_logger().info(f"[{self.drone_id}] All waypoints visited.")
            self._send_status_update("idle")
            self.active = False
            self.current_target = None
            return

        waypoint = self.current_waypoints[self.current_index]
        self.current_target = waypoint  # Save target

        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = "map"  # Adjust if needed
        pose.pose.position.x = waypoint.lat  # Assuming local coordinates
        pose.pose.position.y = waypoint.lon
        pose.pose.position.z = waypoint.alt

        self.setpoint_pub.publish(pose)
        self.get_logger().info(f"Published waypoint {waypoint.id} to /offboard_setpoint_pose")

    def position_callback(self, msg: VehicleLocalPosition):
        if not self.active or self.current_target is None:
            return

        dx = self.current_target.lat - msg.x
        dy = self.current_target.lon - msg.y
        dz = self.current_target.alt - msg.z
        dist = math.sqrt(dx**2 + dy**2 + dz**2)

        if dist <= self.reached_threshold:
            self.get_logger().info(f"Reached waypoint {self.current_target.id} (within {dist:.2f}m)")
            update = WaypointVisited()
            update.drone_id = self.drone_id
            update.waypoint_id = self.current_target.id
            self.waypoint_update_pub.publish(update)

            self.current_index += 1
            self._publish_next_waypoint()


def main(args=None):
    rclpy.init(args=args)
    node = MissionHandlerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
