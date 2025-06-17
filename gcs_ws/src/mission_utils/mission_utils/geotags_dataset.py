import rclpy
from rclpy.node import Node
import math
import json
import xml.etree.ElementTree as ET

from drone_interfaces.msg import Geotag
from geographiclib.geodesic import Geodesic


class GlobalGeotagLogger(Node):
    def __init__(self):
        super().__init__('global_geotag_logger')

        self.declare_parameter('kml_file_path', '')
        kml_file_path = self.get_parameter('kml_file_path').get_parameter_value().string_value

        self.origin_lat, self.origin_lon, self.origin_alt = self.load_origin_from_kml(kml_file_path)

        self.get_logger().info(f"Origin set to: lat={self.origin_lat}, lon={self.origin_lon}, alt={self.origin_alt}")

        self.geotags = []
        self.declare_parameter('geotag_file_path', 'geotags.json')
        self.output_file = self.get_parameter('geotag_file_path').get_parameter_value().string_value


        self.subscription = self.create_subscription(
            Geotag,
            '/drone_1/geotag_generated',
            self.geotag_callback,
            10
        )

    def load_origin_from_kml(self, kml_path):
        tree = ET.parse(kml_path)
        root = tree.getroot()

        # Namespace handling
        ns = {'kml': 'http://www.opengis.net/kml/2.2'}
        coords = root.find('.//kml:coordinates', ns)

        if coords is None:
            raise ValueError("No coordinates found in KML file.")

        lon_str, lat_str, alt_str = coords.text.strip().split(',')[:3]
        return float(lat_str), float(lon_str), float(alt_str)

    def geotag_callback(self, msg):
        # Convert local x, y to lat, lon
        azimuth = math.degrees(math.atan2(msg.x, msg.y))
        horizontal_distance = math.hypot(msg.x, msg.y)

        result = Geodesic.WGS84.Direct(self.origin_lat, self.origin_lon, azimuth, horizontal_distance)
        lat = result['lat2']
        lon = result['lon2']
        alt = self.origin_alt - msg.z  # z is NED (down)

        tag = {
            "id": msg.id,
            "lat": lat,
            "lon": lon,
            "alt": alt,
            "severity_score": msg.severity_score
        }

        self.geotags.append(tag)

        with open(self.output_file, 'w') as f:
            json.dump(self.geotags, f, indent=2)

        self.get_logger().info(f"Saved geotag {msg.id} at lat={lat:.6f}, lon={lon:.6f}, alt={alt:.2f}")



def main(args=None):
    rclpy.init(args=args)
    node = GlobalGeotagLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
