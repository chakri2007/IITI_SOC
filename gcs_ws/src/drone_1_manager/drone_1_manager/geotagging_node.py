import rclpy
from rclpy.node import Node
import math
import random
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

from px4_msgs.msg import VehicleLocalPosition
from drone_interfaces.msg import DroneStatus, Geotag
from pyproj import Proj, transform


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

        self.origin_set = False
        self.origin_lat = None
        self.origin_lon = None
        self.origin_alt = None
        self.local_proj = None
        self.global_proj = Proj(proj='latlong', datum='WGS84')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.subscription_status = self.create_subscription(
            DroneStatus,
            '/drone_1/status',
            self.status_callback,
            10
        )

        self.subscription_position = self.create_subscription(
            VehicleLocalPosition,
            '/px4_1/fmu/out/vehicle_local_position',
            self.position_callback,
            qos_profile
        )

        self.publisher = self.create_publisher(Geotag, '/drone_1/geotag_generated', 10)

        self.get_logger().info("GPS-based geotagging node started.")

    def status_callback(self, msg):
        self.active = (msg.type.lower() == 'surveillance' and msg.status.lower() == 'executing')

    def position_callback(self, msg):
        if not self.active or not msg.xy_valid:
            return

        if not self.origin_set and msg.ref_lat != 0.0 and msg.ref_lon != 0.0:
            self.origin_lat = msg.ref_lat
            self.origin_lon = msg.ref_lon
            self.origin_alt = msg.ref_alt
            self.local_proj = Proj(proj='aeqd', lat_0=self.origin_lat, lon_0=self.origin_lon, datum='WGS84')
            self.origin_set = True
            self.get_logger().info(f"Geotagging origin set to: lat={self.origin_lat}, lon={self.origin_lon}, alt={self.origin_alt}")

        if not self.origin_set:
            self.get_logger().warn("Waiting for origin GPS to be set...")
            return

        current_local = (msg.x, msg.y, msg.z)

        if self.last_tag_position is None:
            self.save_geotag(current_local)
            return

        distance = euclidean(current_local, self.last_tag_position)

        if distance >= 25.0:
            self.save_geotag(current_local)

    def save_geotag(self, local_pos):
        x, y, z = local_pos

        try:
            # Convert local ENU to GPS (lat, lon)
            lon, lat = transform(
                self.local_proj,
                self.global_proj,
                y, x  # ENU: x = East, y = North => pyproj: x=E, y=N
            )
            alt = self.origin_alt - z  # Convert down to up

            geotag = Geotag()
            geotag.id = self.geotag_id
            geotag.lat = lat
            geotag.lon = lon
            geotag.alt = alt
            geotag.severity_score = random.randint(1, 5)

            self.publisher.publish(geotag)
            self.last_tag_position = local_pos
            self.geotag_id += 1

            self.get_logger().info(
                f"Published geotag {geotag.id}: lat={lat:.6f}, lon={lon:.6f}, alt={alt:.2f}, severity={geotag.severity_score}"
            )

        except Exception as e:
            self.get_logger().error(f"Failed to convert local to GPS: {str(e)}")


def main(args=None):
    rclpy.init(args=args)
    node = GeotaggingNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
