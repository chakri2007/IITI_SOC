import rclpy
from rclpy.node import Node
import json
import os

from drone_interfaces.msg import Waypoint, WaypointArray, WaypointRequest, WaypointVisited


class WaypointPublisher(Node):
    def __init__(self):
        super().__init__('waypoint_publisher')
        self.get_logger().info('WaypointPublisher node started.')

        self.waypoints_loaded = []
        self.ascending_batches = []
        self.descending_batches = []
        self.assigned_batches_status = {}

<<<<<<< HEAD
        self.declare_parameter('json_file_path', '/Users/burrachakrapani/Documents/IITISOC/mission_files/iiti_waypoints.json')
        self.declare_parameter('batch_size', 5)

        json_file_path = self.get_parameter('json_file_path').get_parameter_value().string_value
        self.batch_size = self.get_parameter('batch_size').get_parameter_value().integer_value

        if not json_file_path:
            self.get_logger().error("JSON file path not set.")
        else:
            self.load_waypoints_from_json(json_file_path)
=======
        self.declare_parameter('json_file_path', '')
        self.declare_parameter('batch_size', 5)

        self.json_file_path = self.get_parameter('json_file_path').get_parameter_value().string_value
        self.batch_size = self.get_parameter('batch_size').get_parameter_value().integer_value

        if not self.json_file_path:
            self.get_logger().error("JSON file path not set.")
            return
>>>>>>> dual_drone

        self.waypoint_request_subscriber = self.create_subscription(
            WaypointRequest,
            '/waypoint_manager/request',
            self.request_callback,
            10
        )

        self.visited_subscriber = self.create_subscription(
            WaypointVisited,
            '/mission_handler/waypoint_visited',
            self.waypoint_visited_callback,
            10
        )

        self.drone_publishers = {}

    def load_waypoints_from_json(self, file_path):
        if not os.path.exists(file_path):
            self.get_logger().error(f"File not found: {file_path}")
            return

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)

<<<<<<< HEAD
=======
            self.waypoints_loaded.clear()
>>>>>>> dual_drone
            for item in data:
                if all(k in item for k in ['id', 'lat', 'lon', 'alt', 'visited']):
                    wp = Waypoint()
                    wp.id = item['id']
                    wp.lat = item['lat']
                    wp.lon = item['lon']
                    wp.alt = item['alt']
                    wp.visited = item['visited']
                    self.waypoints_loaded.append(wp)
                else:
                    self.get_logger().warning(f"Invalid waypoint: {item}")

            self.waypoints_loaded.sort(key=lambda w: w.id)
            self.create_batches()

        except Exception as e:
            self.get_logger().error(f"Error loading JSON: {e}")

    def create_batches(self):
        self.ascending_batches.clear()
        self.descending_batches.clear()
        self.assigned_batches_status.clear()

        batch_num = 1
        for i in range(0, len(self.waypoints_loaded), self.batch_size):
            batch = self.waypoints_loaded[i:i + self.batch_size]
            self.ascending_batches.append((batch_num, batch))
            self.assigned_batches_status[(batch_num, "top")] = None
            batch_num += 1

        reversed_waypoints = sorted(self.waypoints_loaded, key=lambda w: w.id, reverse=True)
        batch_num = 1
        for i in range(0, len(reversed_waypoints), self.batch_size):
            batch = reversed_waypoints[i:i + self.batch_size]
            self.descending_batches.append((batch_num, batch))
            self.assigned_batches_status[(batch_num, "bottom")] = None
            batch_num += 1

    def get_publisher_for_drone(self, drone_id):
        if drone_id not in self.drone_publishers:
            topic = f"/drone/{drone_id}/waypoints"
            self.drone_publishers[drone_id] = self.create_publisher(WaypointArray, topic, 10)
            self.get_logger().info(f"Created publisher for {topic}")
        return self.drone_publishers[drone_id]

    def request_callback(self, msg):
        drone_id = msg.drone_id
        direction = msg.direction.lower()
<<<<<<< HEAD
=======

        # 🔁 Reload latest waypoints from file
        self.load_waypoints_from_json(self.json_file_path)

>>>>>>> dual_drone
        self.get_logger().info(f"Received request from drone '{drone_id}' for direction '{direction}'.")

        target_batches = self.ascending_batches if direction == "top" else self.descending_batches

        for batch_num, batch in target_batches:
<<<<<<< HEAD
            if self.assigned_batches_status[(batch_num, direction)] is None:
                # Found available batch
                self.assigned_batches_status[(batch_num, direction)] = drone_id

                wp_array = WaypointArray()
                wp_array.waypoints = batch
=======
            assigned_drone = self.assigned_batches_status.get((batch_num, direction), None)

            # Allow reuse of batch if drone is same or not yet assigned
            if assigned_drone is None or assigned_drone == drone_id:
                unvisited_wps = [wp for wp in batch if not wp.visited]

                if not unvisited_wps:
                    continue  # All visited, skip batch

                self.assigned_batches_status[(batch_num, direction)] = drone_id

                wp_array = WaypointArray()
                wp_array.waypoints = unvisited_wps
>>>>>>> dual_drone

                pub = self.get_publisher_for_drone(drone_id)
                pub.publish(wp_array)

<<<<<<< HEAD
                self.get_logger().info(f"Published batch {batch_num} ({direction}) to drone '{drone_id}'")
                return

        self.get_logger().info(f"No unassigned '{direction}' batches available for drone '{drone_id}'.")

    def waypoint_visited_callback(self, msg: WaypointVisited):
        found = False
=======
                self.get_logger().info(
                    f"Published {len(unvisited_wps)} unvisited waypoints from batch {batch_num} ({direction}) to drone '{drone_id}'"
                )
                return

        self.get_logger().info(f"No unvisited '{direction}' waypoints available for drone '{drone_id}'.")

    def waypoint_visited_callback(self, msg: WaypointVisited):
>>>>>>> dual_drone
        for wp in self.waypoints_loaded:
            if wp.id == msg.waypoint_id:
                if not wp.visited:
                    wp.visited = True
                    self.get_logger().info(f"Waypoint ID {wp.id} marked visited by drone {msg.drone_id}")
                else:
                    self.get_logger().info(f"Waypoint ID {wp.id} already visited.")
<<<<<<< HEAD
                found = True
                break

        if not found:
            self.get_logger().warning(f"Waypoint ID {msg.waypoint_id} not found.")
=======
                return

        self.get_logger().warning(f"Waypoint ID {msg.waypoint_id} not found in memory.")
>>>>>>> dual_drone


def main(args=None):
    rclpy.init(args=args)
    node = WaypointPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
