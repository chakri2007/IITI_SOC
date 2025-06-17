import rclpy
from rclpy.node import Node
import math
import random

from px4_msgs.msg import VehicleLocalPosition
from drone_interfaces.msg import DroneStatus, Geotag


def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 +
                     (p1[1] - p2[1])**2 +
                     (p1[2] - p2[2])**2)


class GeotaggingNode(Node):
    def __init__(self):
        super().__init__('geotagging_node')

        self.active = False
        self.last_tag_position = None
        self.geotag_id = 0

        # Subscribe to status updates
        self.subscription_status = self.create_subscription(
            DroneStatus,
            '/drone_1/status',
            self.status_callback,
            10
        )

        # Subscribe to PX4 local position
        self.subscription_position = self.create_subscription(
            VehicleLocalPosition,
            '/fmu/out/vehicle_local_position',
            self.position_callback,
            10
        )

        self.publisher = self.create_publisher(Geotag, '/drone_1/geotag_generated', 10)

        self.get_logger().info("PX4-based local geotagging node started.")

    def status_callback(self, msg):
        self.active = (msg.type.lower() == 'surveillance' and msg.status.lower() == 'executing')

    def position_callback(self, msg):
        if not self.active:
            return

        # Check if position data is valid (according to PX4)
        if not msg.xy_valid:
            self.get_logger().warn("Local XY position not valid.")
            return

        current_pos = (msg.x, msg.y, msg.z)

        if self.last_tag_position is None:
            self.save_geotag(current_pos)
            return

        distance = euclidean(current_pos, self.last_tag_position)

        if distance >= 25.0:
            self.save_geotag(current_pos)

    def save_geotag(self, position):
        geotag = Geotag()
        geotag.id = self.geotag_id
        geotag.x = position[0]
        geotag.y = position[1]
        geotag.z = position[2]
        geotag.severity_score = random.randint(1, 5)

        self.publisher.publish(geotag)
        self.last_tag_position = position
        self.geotag_id += 1

        self.get_logger().info(
            f"Published geotag {geotag.id} at x={geotag.x:.2f}, y={geotag.y:.2f}, z={geotag.z:.2f}, severity={geotag.severity_score}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = GeotaggingNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
