import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import json
import os
import threading

from drone_interfaces.msg import GeotagVisited


class GeotagUpdaterNode(Node):

    def __init__(self):
        super().__init__('geotags_visited_updater')

        self.declare_parameter('geotag_file_path', '/home/chakrapani/drone_files/IITI_SOC/gcs_ws/mission_files/geotags.json')

        self.lock = threading.Lock()

        self.create_subscription(
            GeotagVisited,
            '/mission_handler/geotag_visited',
            self.visited_callback,
            10
        )

        self.get_logger().info("Geotag Updater Node initialized.")

    def visited_callback(self, msg: GeotagVisited):
        geotag_id = msg.geotag_id
        drone_id = msg.drone_id

        self.get_logger().info(f"Received visited confirmation from {drone_id} for Geotag ID: {geotag_id}")

        with self.lock:
            path = self.get_parameter('geotag_file_path').get_parameter_value().string_value
            if not os.path.exists(path):
                self.get_logger().error(f"Geotag JSON file not found at {path}")
                return

            try:
                with open(path, 'r') as f:
                    data = json.load(f)

                updated = False
                for item in data:
                    if 'id' in item and item['id'] == geotag_id:
                        if not item.get('irrigated', False):
                            item['irrigated'] = True
                            updated = True
                            self.get_logger().info(f"Marked Geotag ID {geotag_id} as irrigated.")
                        break

                if updated:
                    tmp_path = path + ".tmp"
                    with open(tmp_path, 'w') as f:
                        json.dump(data, f, indent=2)
                    os.replace(tmp_path, path)
                else:
                    self.get_logger().info(f"Geotag ID {geotag_id} was already marked irrigated or not found.")

            except Exception as e:
                self.get_logger().error(f"Error updating geotags in file: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = GeotagUpdaterNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
