import xml.etree.ElementTree as ET
import re
import json
import os

def kml_to_waypoints_json(kml_filepath):
    waypoints = []
    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

    if not os.path.exists(kml_filepath):
        print(f"Error: KML file not found at '{kml_filepath}'")
        return []

    try:
        tree = ET.parse(kml_filepath)
        root = tree.getroot()

        # Find all Placemark elements within the 'Items' Folder
        # Using the namespace for correct parsing
        for placemark in root.findall(".//kml:Folder/kml:Placemark", namespace):
            name_element = placemark.find("kml:name", namespace)
            description_element = placemark.find("kml:description", namespace)
            point_element = placemark.find("kml:Point/kml:coordinates", namespace)

            if name_element is not None and description_element is not None and point_element is not None:
                # Extract ID from the 'name' tag. It often contains a number like "0 " or "2 Takeoff"
                # We'll use a regex to extract just the leading number
                id_match = re.match(r'(\d+)', name_element.text.strip())
                if id_match:
                    waypoint_id = int(id_match.group(1))
                else:
                    # If ID cannot be parsed, skip this placemark
                    print(f"Warning: Could not parse ID from name '{name_element.text}', skipping placemark.")
                    continue 

                # Extract Lat, Lon, Alt from the 'coordinates' tag
                # Format is Lon,Lat,Alt in KML Point coordinates
                coordinates_text = point_element.text.strip()
                try:
                    lon_str, lat_str, alt_str = coordinates_text.split(',')
                    lat = float(lat_str)
                    lon = float(lon_str)
                    alt = float(alt_str) # Altitude is already in meters, matching your request for 'alt'
                except ValueError:
                    # Handle cases where coordinates might be malformed
                    print(f"Warning: Could not parse coordinates '{coordinates_text}' for waypoint ID {waypoint_id}, skipping placemark.")
                    continue

                waypoints.append({
                    "id": waypoint_id,
                    "lat": lat,
                    "lon": lon,
                    "alt": alt,
                    "visited": False # As this is a plan, assume not visited
                })
    except ET.ParseError as e:
        print(f"Error parsing KML data from '{kml_filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing '{kml_filepath}': {e}")

    # Sort waypoints by their ID to ensure consistent order in the output JSON
    waypoints.sort(key=lambda x: x['id'])

    return waypoints

def save_json_to_file(data, output_filepath):

    try:
        # Create directory if it doesn't exist
        output_dir = os.path.dirname(output_filepath)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2) # indent=2 for pretty printing
        print(f"JSON data successfully saved to '{output_filepath}'")
    except IOError as e:
        print(f"Error saving JSON to '{output_filepath}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving JSON: {e}")

if __name__ == "__main__":
    # --- How to use ---
    # Replace these with your actual file paths
    input_kml_file = "/Users/burrachakrapani/Documents/IITISOC/mission_files/iit.kml"
    output_json_file = "/Users/burrachakrapani/Documents/IITISOC/mission_files/iiti_waypoints.json"

    # Convert the KML and get the waypoints list
    extracted_waypoints = kml_to_waypoints_json(input_kml_file)

    # If waypoints were successfully extracted, save them to a JSON file
    if extracted_waypoints:
        save_json_to_file(extracted_waypoints, output_json_file)
    else:
        print("No waypoints were extracted. The JSON file was not created.")