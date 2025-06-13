import xml.etree.ElementTree as ET
import re
import json
import os
import math

# Earth's radius and flattening for WGS-84
R_EARTH = 6378137.0          # radius in meters
F_EARTH = 1 / 298.257223563  # flattening
E_SQ = F_EARTH * (2 - F_EARTH)

def geodetic_to_ned(lat, lon, alt, origin_lat, origin_lon, origin_alt):
    # Convert degrees to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    origin_lat_rad = math.radians(origin_lat)
    origin_lon_rad = math.radians(origin_lon)

    d_lat = lat_rad - origin_lat_rad
    d_lon = lon_rad - origin_lon_rad

    # Radius of curvature in the prime vertical
    sin_lat = math.sin(origin_lat_rad)
    N = R_EARTH / math.sqrt(1 - E_SQ * sin_lat * sin_lat)

    # Calculate local displacements
    north = d_lat * (N + origin_alt)
    east = d_lon * (N + origin_alt) * math.cos(origin_lat_rad)
    down = origin_alt - alt  # down is positive downward

    return north, east, down

def kml_to_ned_waypoints_json(kml_filepath):
    waypoints = []
    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

    if not os.path.exists(kml_filepath):
        print(f"Error: KML file not found at '{kml_filepath}'")
        return []

    origin_lat = origin_lon = origin_alt = None

    try:
        tree = ET.parse(kml_filepath)
        root = tree.getroot()

        for placemark in root.findall(".//kml:Folder/kml:Placemark", namespace):
            name_element = placemark.find("kml:name", namespace)
            point_element = placemark.find("kml:Point/kml:coordinates", namespace)

            if name_element is not None and point_element is not None:
                id_match = re.match(r'(\d+)', name_element.text.strip())
                if id_match:
                    waypoint_id = int(id_match.group(1))
                else:
                    print(f"Warning: Could not parse ID from name '{name_element.text}', skipping.")
                    continue

                coordinates_text = point_element.text.strip()
                try:
                    lon_str, lat_str, alt_str = coordinates_text.split(',')
                    lat = float(lat_str)
                    lon = float(lon_str)
                    alt = float(alt_str)
                except ValueError:
                    print(f"Warning: Could not parse coordinates '{coordinates_text}' for ID {waypoint_id}. Skipping.")
                    continue

                # First point is origin
                if origin_lat is None:
                    origin_lat, origin_lon, origin_alt = lat, lon, alt

                north, east, down = geodetic_to_ned(lat, lon, alt, origin_lat, origin_lon, origin_alt)

                waypoints.append({
                    "id": waypoint_id,
                    "north": north,
                    "east": east,
                    "down": down,
                    "visited": False
                })

    except ET.ParseError as e:
        print(f"Error parsing KML: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    waypoints.sort(key=lambda x: x['id'])
    return waypoints

def save_json_to_file(data, output_filepath):
    try:
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Saved to '{output_filepath}'")
    except Exception as e:
        print(f"Error saving JSON: {e}")

if __name__ == "__main__":
    input_kml_file = "/Users/burrachakrapani/Documents/IITISOC/mission_files/iit.kml"
    output_json_file = "/Users/burrachakrapani/Documents/IITISOC/mission_files/iiti_waypoints_ned.json"

    extracted_ned_waypoints = kml_to_ned_waypoints_json(input_kml_file)

    if extracted_ned_waypoints:
        save_json_to_file(extracted_ned_waypoints, output_json_file)
    else:
        print("No waypoints extracted. JSON not created.")
