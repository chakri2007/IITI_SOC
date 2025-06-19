import rclpy
from rclpy.node import Node
import json
from drone_interfaces.msg import Geotag


class GlobalGeotagLogger(Node):
    def __init__(self):
        super().__init__('global_geotag_logger')

        # Output file parameter
        self.declare_parameter('geotag_file_path', 'geotags.json')
        self.output_file = self.get_parameter('geotag_file_path').get_parameter_value().string_value

        self.geotags = []

        # Subscription to GPS-based geotags
        self.subscription = self.create_subscription(
            Geotag,
            '/drone_1/geotag_generated',
            self.geotag_callback,
            10
        )

        self.get_logger().info(f"Geotag logger started. Saving to: {self.output_file}")

    def geotag_callback(self, msg):
        tag = {
            "id": msg.id,
            "lat": msg.lat,
            "lon": msg.lon,
            "alt": msg.alt,
            "severity_score": msg.severity_score
        }

        self.geotags.append(tag)

        # Write updated list to file
        with open(self.output_file, 'w') as f:
            json.dump(self.geotags, f, indent=2)

        self.get_logger().info(
            f"Saved geotag {msg.id} at lat={msg.lat:.6f}, lon={msg.lon:.6f}, alt={msg.alt:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = GlobalGeotagLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
