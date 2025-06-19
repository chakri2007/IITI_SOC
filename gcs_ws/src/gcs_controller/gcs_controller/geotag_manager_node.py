import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import threading
import json
import os

from drone_interfaces.msg import Geotag, GeotagArray, GeotagRequest


class GeotagNode(Node):

    def __init__(self):
        super().__init__('geotag_node')

        self.declare_parameter('json_file_path', '')
        self.declare_parameter('batch_size', 5)

        self.lock = threading.Lock()
        self.geotag_list = []  # stores received geotags
        self.sent_indices = {}  # (drone_id, direction) -> index
        self._pub_cache = {}  # Avoid name conflict with rclpy.Node's internal 'publishers'

        self.subscriber = self.create_subscription(
            Geotag,
            '/geotag_generated',
            self.geotag_callback,
            10
        )

        self.request_subscriber = self.create_subscription(
            GeotagRequest,
            '/geotag_manager/request',
            self.request_callback,
            10
        )

        self.get_logger().info("Geotag Node started with ID filtering from JSON.")

    def geotag_callback(self, msg: Geotag):
        with self.lock:
            # Avoid duplicates (check by ID)
            if not any(g.id == msg.id for g in self.geotag_list):
                self.geotag_list.append(msg)
                self.get_logger().info(f"Stored Geotag ID {msg.id}")
            else:
                self.get_logger().info(f"Duplicate Geotag ID {msg.id} ignored")

    def get_irrigated_ids_from_json(self):
        path = self.get_parameter('json_file_path').get_parameter_value().string_value
        if not os.path.exists(path):
            self.get_logger().error(f"Geotag JSON file not found at {path}")
            return set()

        try:
            with open(path, 'r') as f:
                data = json.load(f)
            return {item['id'] for item in data if item.get('irrigated') is True}
        except Exception as e:
            self.get_logger().error(f"Error reading irrigated geotag IDs: {e}")
            return set()

    def request_callback(self, msg: GeotagRequest):
        drone_id = msg.drone_id
        direction = msg.direction.lower()
        key = (drone_id, direction)
        batch_size = self.get_parameter('batch_size').get_parameter_value().integer_value

        with self.lock:
            # Filter out irrigated points based on JSON file
            irrigated_ids = self.get_irrigated_ids_from_json()
            before = len(self.geotag_list)
            self.geotag_list = [g for g in self.geotag_list if g.id not in irrigated_ids]
            after = len(self.geotag_list)
            self.get_logger().info(f"Filtered {before - after} irrigated geotags. Remaining: {after}")

            if not self.geotag_list:
                self.get_logger().warn("No geotags to send after filtering.")
                return

            sorted_geotags = sorted(
                self.geotag_list,
                key=lambda g: g.id,
                reverse=(direction == 'bottom')
            )

            start_idx = self.sent_indices.get(key, 0)
            end_idx = start_idx + batch_size

            if start_idx >= len(sorted_geotags):
                self.get_logger().info(f"No more geotags for drone {drone_id} in direction {direction}")
                return

            batch = sorted_geotags[start_idx:end_idx]
            self.sent_indices[key] = end_idx

        # Publish the batch
        geotag_array = GeotagArray()
        geotag_array.geotags = batch

        topic_name = f"/geotags_array"
        if topic_name not in self._pub_cache:
            self._pub_cache[topic_name] = self.create_publisher(GeotagArray, topic_name, 10)

        self._pub_cache[topic_name].publish(geotag_array)
        self.get_logger().info(f"Sent geotag IDs {[g.id for g in batch]} to {topic_name} ({direction})")


def main(args=None):
    rclpy.init(args=args)
    node = GeotagNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
