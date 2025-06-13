import rclpy
from rclpy.node import Node

from drone_interfaces.msg import Waypoint, WaypointArray, WaypointVisited, DroneStatusUpdate
from px4_msgs.msg import VehicleCommand


class MissionHandlerNode(Node):

    def __init__(self):
        super().__init__('mission_handler_node')
        self.get_logger().info("Mission Handler Node Started.")

        self.current_waypoints = []
        self.current_index = 0
        self.active = False
        self.drone_id = 'drone_1'

        self.create_subscription(WaypointArray, f'/drone/{self.drone_id}/waypoints', self.waypoint_callback, 10)

        self.px4_command_pub = self.create_publisher(VehicleCommand, '/fmu/in/vehicle_command', 10)
        self.waypoint_update_pub = self.create_publisher(WaypointVisited, '/mission_handler/waypoint_visited', 10)
        self.status_update_pub = self.create_publisher(DroneStatusUpdate, f'/{self.drone_id}/update_status', 10)

        self.timer = self.create_timer(2.0, self.execute_mission)

        self._send_status_update("idle")  # Initial state

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

    def execute_mission(self):
        if not self.active or self.current_index >= len(self.current_waypoints):
            if not self.active and self.current_index > 0:
                self.get_logger().debug(f"[{self.drone_id}] Mission complete.")
            return

        waypoint = self.current_waypoints[self.current_index]
        self.get_logger().info(f"Going to waypoint {self.current_index + 1}/{len(self.current_waypoints)}: "
                               f"[Lat: {waypoint.lat}, Lon: {waypoint.lon}, Alt: {waypoint.alt}]")

        cmd = VehicleCommand()
        cmd.param5 = float(waypoint.lat)
        cmd.param6 = float(waypoint.lon)
        cmd.param7 = float(waypoint.alt)
        cmd.command = VehicleCommand.VEHICLE_CMD_NAV_WAYPOINT
        cmd.target_system = 1
        cmd.target_component = 1
        cmd.source_system = 1
        cmd.source_component = 1
        cmd.from_external = True
        cmd.timestamp = int(self.get_clock().now().nanoseconds / 1000)

        self.px4_command_pub.publish(cmd)

        self.get_logger().info(f"Reached waypoint {waypoint.id} (simulated)")

        update = WaypointVisited()
        update.drone_id = self.drone_id
        update.waypoint_id = waypoint.id
        self.waypoint_update_pub.publish(update)

        self.current_index += 1

        if self.current_index >= len(self.current_waypoints):
            self.get_logger().info(f"[{self.drone_id}] All waypoints visited.")
            self._send_status_update("idle")
            self.active = False


def main(args=None):
    rclpy.init(args=args)
    node = MissionHandlerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
