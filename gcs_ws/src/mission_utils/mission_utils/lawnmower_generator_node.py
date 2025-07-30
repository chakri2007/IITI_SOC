import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import VehicleLocalPosition

import json
import math
import os
from shapely.geometry import Polygon, LineString, Point
from shapely import affinity
from pyproj import Transformer
import xml.etree.ElementTree as ET


class LawnmowerGeneratorNode(Node):
    def __init__(self):
        super().__init__('lawnmower_generator_node')
        self.get_logger().info('Lawnmower Generator Node has started. Waiting for home position...')


        # Declare parameters
        self.declare_parameter('kml_file_path', '')
        self.declare_parameter('output_file', '')
        self.declare_parameter('spacing', 10.0)
        self.declare_parameter('turnaround', 3.0)
        self.declare_parameter('start_from', 'top')
        self.declare_parameter('altitude', 640.0)

        self.delete_old_json_files()

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.subscription = self.create_subscription(
            VehicleLocalPosition,
            '/px4_1/fmu/out/vehicle_local_position',
            self.local_position_callback,
            qos_profile
        )

        self.received_position = False
    
    def delete_old_json_files(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            gcs_ws_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
            workspace_root = os.path.expanduser('~/IITISoC-25-IVR09/gcs_ws')

            waypoint_path = os.path.join(workspace_root, 'mission_files', 'iiti_waypoints.json')
            geotag_path = os.path.join(workspace_root, 'mission_files', 'geotags.json')

            if os.path.exists(waypoint_path):
                os.remove(waypoint_path)
                self.get_logger().info(f"Deleted old waypoint file: {waypoint_path}")    

            if os.path.exists(geotag_path):
                os.remove(geotag_path)
                self.get_logger().info(f"Deleted old geotag file: {geotag_path}")

        except Exception as e:
            self.get_logger().warn(f"Failed to delete old JSON files: {e}")
    
        
    def local_position_callback(self, msg):

        if not self.received_position:
            self.received_position = True
            self.ref_lat = msg.ref_lat
            self.ref_lon = msg.ref_lon
            self.ref_alt = msg.ref_alt
            self.get_logger().info(f"Received Home Position: lat={self.ref_lat}, lon={self.ref_lon}, alt={self.ref_alt}")
            self.generate_path()

    def generate_path(self):
        # Get parameters
        kml_file_path = self.get_parameter('kml_file_path').get_parameter_value().string_value
        output_file = self.get_parameter('output_file').get_parameter_value().string_value
        spacing = self.get_parameter('spacing').get_parameter_value().double_value
        turnaround = self.get_parameter('turnaround').get_parameter_value().double_value
        start_from = self.get_parameter('start_from').get_parameter_value().string_value
        altitude = self.get_parameter('altitude').get_parameter_value().double_value

        coords = self.read_kml_boundary(kml_file_path)
        if not coords:
            self.get_logger().error('Could not extract boundary from KML.')
            return
        self.get_logger().info(f"KML boundary extracted with {len(coords)} points.")

        xy_coords = self.convert_gps_to_xy(coords)
        polygon = Polygon(xy_coords)
        sweep_angle = self.get_longest_side_angle(xy_coords)

        passes = self.generate_lawnmower_passes(polygon, spacing, turnaround, sweep_angle)
        self.get_logger().info(f"Generated {len(passes)} lawnmower passes.")

        # Find farthest of 4 endpoints from home position
        home_xy = self.convert_gps_to_xy([(self.ref_lon, self.ref_lat)])[0]
        farthest_point, reverse_path = self.find_farthest_endpoint(passes, home_xy)

        # Create ordered waypoints list
        waypoints = []
        passes_to_use = passes if not reverse_path else passes[::-1]
        toggle = False
        for line in passes_to_use:
            coords = list(line.coords)
            coords = coords if not toggle else coords[::-1]
            waypoints.extend(coords)
            toggle = not toggle

        gps_waypoints = self.convert_xy_to_gps(waypoints)
        self.get_logger().info(f"Total waypoints generated: {len(gps_waypoints)}")

        self.save_waypoints_to_json(gps_waypoints, output_file, altitude)


    def read_kml_boundary(self, kml_filepath):
        namespace = {'kml': 'http://www.opengis.net/kml/2.2'}
        if not os.path.exists(kml_filepath):
            self.get_logger().error(f"KML file not found: {kml_filepath}")
            return None
        try:
            tree = ET.parse(kml_filepath)
            root = tree.getroot()
            polygon_coords = root.find(".//kml:Polygon/kml:outerBoundaryIs/kml:LinearRing/kml:coordinates", namespace)
            if polygon_coords is None:
                self.get_logger().error("No polygon found in KML.")
                return None

            coord_text = polygon_coords.text.strip()
            coords = []
            for line in coord_text.split():
                lon_str, lat_str, *_ = line.split(',')
                coords.append((float(lon_str), float(lat_str)))

            if coords[0] != coords[-1]:
                coords.append(coords[0])
            return coords
        except Exception as e:
            self.get_logger().error(f"Error reading KML: {e}")
            return None

    def convert_gps_to_xy(self, coords):
        transformer = Transformer.from_crs("epsg:4326", "epsg:3857", always_xy=True)
        return [transformer.transform(lon, lat) for lon, lat in coords]

    def convert_xy_to_gps(self, xy_coords):
        transformer = Transformer.from_crs("epsg:3857", "epsg:4326", always_xy=True)
        return [transformer.transform(x, y) for x, y in xy_coords]

    def get_longest_side_angle(self, coords):
        max_len = 0
        best_angle = 0
        for i in range(len(coords) - 1):
            x1, y1 = coords[i]
            x2, y2 = coords[i + 1]
            dx = x2 - x1
            dy = y2 - y1
            length = math.hypot(dx, dy)
            angle = math.degrees(math.atan2(dy, dx))
            if length > max_len:
                max_len = length
                best_angle = angle
        return best_angle

    def generate_lawnmower_passes(self, polygon, spacing, turnaround, sweep_angle):
        rotated = affinity.rotate(polygon, -sweep_angle, origin='centroid')
        minx, miny, maxx, maxy = rotated.bounds

        y = maxy + turnaround
        lines = []
        while y > miny - turnaround:
            line = LineString([(minx - turnaround, y), (maxx + turnaround, y)])
            clipped = line.intersection(rotated)
            if not clipped.is_empty:
                if clipped.geom_type == 'LineString':
                    lines.append(clipped)
                elif clipped.geom_type == 'MultiLineString':
                    lines.extend(clipped.geoms)
            y -= spacing

        final_passes = [affinity.rotate(line, sweep_angle, origin=polygon.centroid) for line in lines]
        return final_passes

    def find_farthest_endpoint(self, passes, home_xy):
        points_to_check = []
        if passes:
            points_to_check.append(passes[0].coords[0])
            points_to_check.append(passes[0].coords[-1])
            points_to_check.append(passes[-1].coords[0])
            points_to_check.append(passes[-1].coords[-1])

        farthest_point = None
        max_dist = -1
        reverse_path = False

        for idx, pt in enumerate(points_to_check):
            dist = math.hypot(pt[0] - home_xy[0], pt[1] - home_xy[1])
            if dist > max_dist:
                max_dist = dist
                farthest_point = pt
                reverse_path = idx >= 2  # If it's from last pass, we reverse
        return farthest_point, reverse_path
      
    def save_waypoints_to_json(self, gps_waypoints, output_file, altitude):
        json_data = [
            {
                "id": i + 1,
                "lat": lat,
                "lon": lon,
                "alt": altitude,
                "visited": False
            }
            for i, (lon, lat) in enumerate(gps_waypoints)
        ]

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4)
        self.get_logger().info(f"Lawnmower path saved to {output_file}")
   
	        


def main(args=None):
    rclpy.init(args=args)
    node = LawnmowerGeneratorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()