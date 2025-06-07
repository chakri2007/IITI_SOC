import rclpy
from rclpy.node import Node
from drone_interfaces.msg import Waypoint, WaypointArray, WaypointUpdate, StatusUpdate
from px4_msgs.msg import VehicleCommand
import time


class MissionHandlerNode(Node):

    def __init__(self):
        super().__init__('mission_handler_node')
        self.get_logger().info("Mission Handler Node Started.")

        self.current_waypoints = []
        self.current_index = 0
        self.active = False
        self.drone_id = 'drone_1'  # Changeable if needed

        # Subscribers
        self.create_subscription(WaypointArray, '/drone/drone_1/waypoints', self.waypoint_callback, 10)

        # Publishers
        self.px4_command_pub = self.create_publisher(VehicleCommand, '/fmu/in/vehicle_command', 10)
        self.waypoint_update_pub = self.create_publisher(WaypointUpdate, '/mission_handler/waypoint_visited', 10)
        self.status_update_pub = self.create_publisher(StatusUpdate, '/status_publisher/update_status', 10)

        # Timer for simulating waypoint arrival
        self.timer = self.create_timer(2.0, self.execute_mission)

    def waypoint_callback(self, msg: WaypointArray):
        if not msg.waypoints:
            self.get_logger().warn("Received empty waypoint list.")
            return

        self.get_logger().info(f"Received {len(msg.waypoints)} waypoints.")
        self.current_waypoints = msg.waypoints
        self.current_index = 0
        self.active = True

    def execute_mission(self):
        if not self.active or self.current_index >= len(self.current_waypoints):
            return

        waypoint = self.current_waypoints[self.current_index]
        self.get_logger().info(f"Going to waypoint {self.current_index + 1}: "
                               f"[Lat: {waypoint.latitude}, Lon: {waypoint.longitude}, Alt: {waypoint.altitude}]")

        # Send command to PX4
        cmd = VehicleCommand()
        cmd.param5 = waypoint.latitude
        cmd.param6 = waypoint.longitude
        cmd.param7 = waypoint.altitude
        cmd.command = VehicleCommand.VEHICLE_CMD_NAV_WAYPOINT
        cmd.target_system = 1
        cmd.target_component = 1
        cmd.source_system = 1
        cmd.source_component = 1
        cmd.from_external = True
        cmd.timestamp = int(time.time() * 1e6)

        self.px4_command_pub.publish(cmd)

        # Simulate reaching the waypoint (you'll replace this with actual feedback logic)
        self.get_logger().info(f"Reached waypoint {self.current_index + 1}")

        # Notify supervisor
        waypoint_update = WaypointUpdate()
        waypoint_update.drone_id = self.drone_id
        waypoint_update.index = self.current_index
        waypoint_update.visited = True
        self.waypoint_update_pub.publish(waypoint_update)

        self.current_index += 1

        # All waypoints visited
        if self.current_index >= len(self.current_waypoints):
            self.get_logger().info("All waypoints visited. Sending status: idle")

            status_msg = StatusUpdate()
            status_msg.drone_id = self.drone_id
            status_msg.status = "idle"
            self.status_update_pub.publish(status_msg)

            self.active = False


def main(args=None):
    rclpy.init(args=args)
    node = MissionHandlerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
