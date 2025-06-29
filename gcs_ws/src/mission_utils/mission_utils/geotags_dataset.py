import rclpy
from rclpy.node import Node
import json
import os

from drone_interfaces.msg import Geotag


class GlobalGeotagLogger(Node):
    def __init__(self):
        super().__init__('global_geotag_logger')

        # Output file parameter
        self.declare_parameter('geotag_file_path', 'geotags.json')
        self.output_file = self.get_parameter('geotag_file_path').get_parameter_value().string_value

        # Ensure file exists
        if not os.path.exists(self.output_file):
            with open(self.output_file, 'w') as f:
                json.dump([], f)

        # Subscription to GPS-based geotags
        self.subscription = self.create_subscription(
            Geotag,
            '/drone_1/geotag_generated',
            self.geotag_callback,
            10
        )

        self.get_logger().info(f"Geotag logger started. Saving to: {self.output_file}")

    def geotag_callback(self, msg):
        new_tag = {
            "id": msg.id,
            "lat": msg.lat,
            "lon": msg.lon,
            "alt": msg.alt,
            "severity_score": msg.severity_score,
            "irrigated": False
        }

        try:
            # Load current data from file
            with open(self.output_file, 'r') as f:
                existing_tags = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.get_logger().warn(f"Could not load existing geotags: {e}")
            existing_tags = []

        # Check if this ID already exists
        for item in existing_tags:
            if item.get("id") == new_tag["id"]:
                self.get_logger().info(f"Geotag ID {new_tag['id']} already exists. Skipping.")
                return

        # Append new tag and write back to file
        existing_tags.append(new_tag)
        try:
            with open(self.output_file, 'w') as f:
                json.dump(existing_tags, f, indent=2)
            self.get_logger().info(
                f"Saved geotag {msg.id} at lat={msg.lat:.6f}, lon={msg.lon:.6f}, alt={msg.alt:.2f}"
            )
        except Exception as e:
            self.get_logger().error(f"Failed to write updated geotags: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = GlobalGeotagLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
