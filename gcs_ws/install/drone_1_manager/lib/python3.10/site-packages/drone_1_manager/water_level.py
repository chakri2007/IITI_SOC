import rclpy
from rclpy.node import Node
from drone_interfaces.msg import GeotagArray, DroneStatusUpdate, DroneStatus, GeotagVisited
from std_msgs.msg import Float32
import fcntl
import os


class WaterLevelNode(Node):
    def __init__(self):
        super().__init__('water_level_node')

        self.declare_parameter('drone_id', 'drone_1')
        self.drone_id = self.get_parameter('drone_id').get_parameter_value().string_value
        self.full_capacity = 100.0
        self.water_level = self.full_capacity
        self.drone_type = 'unknown'
        self.last_status = 'idle'

        self.geotag_severity_cache = {}  # geotag_id → severity_score

        # Subscriptions
        self.create_subscription(GeotagArray, f'/{self.drone_id}/geotag_array', self.geotag_array_callback, 10)
        self.create_subscription(DroneStatus, f'/{self.drone_id}/status', self.status_callback, 10)
        self.create_subscription(DroneStatusUpdate, f'/{self.drone_id}/update_status', self.status_update_callback, 10)
        self.create_subscription(GeotagVisited, '/mission_handler/geotag_visited', self.geotag_visited_callback, 10)

        # Publisher
        self.water_pub = self.create_publisher(Float32, f'/{self.drone_id}/water_level', 10)
        self.timer = self.create_timer(5.0, self.publish_water_level)

        self.file_path = '/home/bhav/IITISoC-25-IVR09/gcs_ws/mission_files/water_levels.txt'

        self.get_logger().info(f"[{self.drone_id}] WaterLevelNode initialized.")

    def geotag_array_callback(self, msg: GeotagArray):
        if self.drone_type.lower() != 'irrigation':
            return
        for geotag in msg.geotags:
            self.geotag_severity_cache[geotag.id] = geotag.severity_score
            self.get_logger().info(f"Cached severity {geotag.severity_score} for geotag ID {geotag.id}")

    def geotag_visited_callback(self, msg: GeotagVisited):
        if msg.drone_id != self.drone_id:
            return  # Ignore messages from other drones

        geotag_id = msg.geotag_id
        severity = self.geotag_severity_cache.get(geotag_id)

        if severity is None:
            self.get_logger().warn(f"Geotag ID {geotag_id} visited but not found in cache. Ignoring.")
            return

        release_amount = self.compute_release(severity)
        self.water_level = max(0.0, self.water_level - release_amount)
        self.get_logger().info(f"Irrigated Geotag {geotag_id} with severity {severity}. Released {release_amount:.2f} units. Remaining: {self.water_level:.2f}")
        del self.geotag_severity_cache[geotag_id]

        if self.water_level <= 0.0:
            self.get_logger().warn("Water tank is empty!")

    def compute_release(self, severity_score):
        return min(10.0, severity_score * 2.0)

    def status_callback(self, msg: DroneStatus):
        if msg.drone_id == self.drone_id:
            self.drone_type = msg.type.lower()

            if self.drone_type == 'surveillance':
                if self.water_level != 0.0:
                    self.water_level = 0.0
                    self.get_logger().info("Surveillance drone detected. Water level forcibly set to 0.")

    def status_update_callback(self, msg: DroneStatusUpdate):
        if msg.drone_id != self.drone_id:
            return
        if msg.status == 'charged' and self.last_status != 'charged':
            self.water_level = self.full_capacity
            self.get_logger().info("Water tank refilled to full capacity.")
        self.last_status = msg.status

    def publish_water_level(self):
        msg = Float32()
        msg.data = self.water_level
        self.water_pub.publish(msg)
        self.get_logger().debug(f"Published water level: {self.water_level:.2f}")

        # Update shared file
        self.update_water_level_file()

    def update_water_level_file(self):
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'a+') as f:
                fcntl.flock(f, fcntl.LOCK_EX)
                f.seek(0)
                lines = f.readlines()
                updated_lines = []
                found = False
                for line in lines:
                    if line.startswith(f"{self.drone_id} ="):
                        updated_lines.append(f"{self.drone_id} = {self.water_level:.2f}\n")
                        found = True
                    else:
                        updated_lines.append(line)
                if not found:
                    updated_lines.append(f"{self.drone_id} = {self.water_level:.2f}\n")
                f.seek(0)
                f.truncate(0)
                f.writelines(updated_lines)
                fcntl.flock(f, fcntl.LOCK_UN)
        except Exception as e:
            self.get_logger().error(f"Error writing to water level file: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = WaterLevelNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
