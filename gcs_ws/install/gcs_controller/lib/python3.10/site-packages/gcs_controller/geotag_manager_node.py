import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import json
import os
import threading

from drone_interfaces.msg import Geotag, GeotagArray, GeotagRequest


class GeotagManagerNode(Node):

    def __init__(self):
        super().__init__('geotag_manager_node')

        # Declare parameters
        self.declare_parameter('geotag_file_path', '/home/chakrapani/drone_files/IITI_SOC//gcs_ws/mission_files/geotags.json')
        self.declare_parameter('batch_size', 5)

        self.lock = threading.Lock()
        self._pub_cache = {}     # drone_id -> publisher

        # Subscription for batch request
        self.request_subscriber = self.create_subscription(
            GeotagRequest,
            '/geotag_manager/request',
            self.request_callback,
            10
        )

        self.get_logger().info("Geotag Manager Node initialized.")

    def load_unirrigated_geotags_from_file(self):
        """Load geotags from file and return only unirrigated ones (irrigated: false)."""
        path = self.get_parameter('geotag_file_path').get_parameter_value().string_value
        if not os.path.exists(path):
            self.get_logger().error(f"Geotag JSON file not found at {path}")
            return []

        try:
            with open(path, 'r') as f:
                data = json.load(f)

            unirrigated = []
            for item in data:
                if not item.get('irrigated', False):
                    g = Geotag()
                    g.id = item['id']
                    g.lat = item['lat']
                    g.lon = item['lon']
                    g.alt = item['alt']
                    g.severity_score = item['severity_score']
                    unirrigated.append(g)

            self.get_logger().info(f"Found {len(unirrigated)} unirrigated geotags.")
            return unirrigated
        except Exception as e:
            self.get_logger().error(f"Error reading geotags from file: {e}")
            return []

    def request_callback(self, msg: GeotagRequest):
        """Handle incoming batch request for unirrigated geotags."""
        drone_id = msg.drone_id
        direction = msg.direction.lower()
        batch_size = self.get_parameter('batch_size').get_parameter_value().integer_value

        with self.lock:
            all_unirrigated = self.load_unirrigated_geotags_from_file()
            if not all_unirrigated:
                self.get_logger().warn("No unirrigated geotags to send.")
                return

            sorted_geotags = sorted(
                all_unirrigated,
                key=lambda g: g.id,
                reverse=(direction == 'bottom')
            )

            batch = sorted_geotags[:batch_size]
            if not batch:
                self.get_logger().info(f"No unirrigated geotags available for drone {drone_id} in direction '{direction}'")
                return

        # Publish batch to the drone-specific topic
        geotag_array = GeotagArray()
        geotag_array.geotags = batch

        topic_name = f"/{drone_id}/geotag_array"
        if topic_name not in self._pub_cache:
            self._pub_cache[topic_name] = self.create_publisher(GeotagArray, topic_name, 10)

        self._pub_cache[topic_name].publish(geotag_array)
        self.get_logger().info(f"Sent geotag IDs {[g.id for g in batch]} to {topic_name}")


def main(args=None):
    rclpy.init(args=args)
    node = GeotagManagerNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
