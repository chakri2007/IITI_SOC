import rclpy
from rclpy.node import Node
from drone_interfaces.msg import WaypointVisited
import json
import os

class WaypointVisitedUpdater(Node):

    def __init__(self):
        super().__init__('waypoints_dataset')

        self.declare_parameter('waypoint_file_path', '')
        self.waypoint_file_path = self.get_parameter('waypoint_file_path').get_parameter_value().string_value

        self.subscription = self.create_subscription(
            WaypointVisited,
            '/mission_handler/waypoint_visited',
            self.listener_callback,
            10
        )
        self.get_logger().info('WaypointVisitedUpdater Node has started.')
        self.get_logger().info(f"Using waypoint file: {self.waypoint_file_path}")

    def listener_callback(self, msg):
        waypoint_id = msg.waypoint_id
        self.get_logger().info(f"Received waypoint visited update for ID: {waypoint_id}")
        self.update_json_waypoint(waypoint_id)

    def update_json_waypoint(self, waypoint_id):
        if not os.path.exists(self.waypoint_file_path):
            self.get_logger().error(f"Waypoint file '{self.waypoint_file_path}' not found.")
            return

        with open(self.waypoint_file_path, 'r') as f:
            try:
                waypoints = json.load(f)
            except json.JSONDecodeError:
                self.get_logger().error(f"Failed to decode JSON from '{self.waypoint_file_path}'")
                return

        updated = False
        for waypoint in waypoints:
            if waypoint['id'] == waypoint_id:
                if not waypoint.get('visited', False):
                    waypoint['visited'] = True
                    updated = True
                    self.get_logger().info(f"Marked waypoint ID {waypoint_id} as visited.")
                break

        if updated:
            with open(self.waypoint_file_path, 'w') as f:
                json.dump(waypoints, f, indent=2)
        else:
            self.get_logger().warn(f"No update made. Waypoint ID {waypoint_id} was already visited or not found.")

def main(args=None):
    rclpy.init(args=args)
    node = WaypointVisitedUpdater()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
