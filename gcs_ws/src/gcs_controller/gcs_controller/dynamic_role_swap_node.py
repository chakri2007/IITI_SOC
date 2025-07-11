import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32
from drone_interfaces.msg import DroneTypeChange, SurveillanceStatus


class DynamicRoleSwap(Node):
    def __init__(self):
        super().__init__('dynamic_role_swap_node')

        self.swap_done = False  # only one swap allowed (change this if needed)
        self.drone_status = {
            "drone_1": None,
            "drone_2": None
        }
        self.drone_type = {
            "drone_1": "irrigation",     # initial role assumptions
            "drone_2": "surveillance"
        }
        self.water_levels = {
            "drone_1": None,
            "drone_2": None
        }

        # Publishers for type and status updates
        self.type_update_pubs = {
            "drone_1": self.create_publisher(DroneTypeChange, 'drone_1/type_change', 10),
            "drone_2": self.create_publisher(DroneTypeChange, 'drone_2/type_change', 10)
        }
        self.status_update_pubs = {
            "drone_1": self.create_publisher(String, 'drone_1/status', 10),
            "drone_2": self.create_publisher(String, 'drone_2/status', 10)
        }

        # Subscriptions
        self.create_subscription(SurveillanceStatus, 'surveillance_status', self.surveillance_status_callback, 10)
        self.create_subscription(String, 'drone_1/status', self.status_callback_1, 10)
        self.create_subscription(String, 'drone_2/status', self.status_callback_2, 10)
        self.create_subscription(Float32, '/drone_1/water_level', self.water_level_callback_1, 10)
        self.create_subscription(Float32, '/drone_2/water_level', self.water_level_callback_2, 10)

    def surveillance_status_callback(self, msg: SurveillanceStatus):
        if msg.surveillance_completed:
            self.get_logger().info("Surveillance task reported complete.")

    def status_callback_1(self, msg):
        self.drone_status["drone_1"] = msg.data
        self.get_logger().info(f"drone_1 status: {msg.data}")
        self.check_and_swap("drone_1")

    def status_callback_2(self, msg):
        self.drone_status["drone_2"] = msg.data
        self.get_logger().info(f"drone_2 status: {msg.data}")
        self.check_and_swap("drone_2")

    def water_level_callback_1(self, msg):
        self.water_levels["drone_1"] = msg.data
        self.get_logger().info(f"drone_1 water level: {msg.data}")
        self.check_and_swap("drone_1")

    def water_level_callback_2(self, msg):
        self.water_levels["drone_2"] = msg.data
        self.get_logger().info(f"drone_2 water level: {msg.data}")
        self.check_and_swap("drone_2")

    def check_and_swap(self, drone_id):
        if self.swap_done:
            return

        current_type = self.drone_type.get(drone_id)
        current_status = self.drone_status.get(drone_id)
        current_water = self.water_levels.get(drone_id)

        # Debug log
        self.get_logger().info(
            f"[CHECK] {drone_id} — Type: {current_type}, Status: {current_status}, Water: {current_water}"
        )

        if (
            current_type == "irrigation" and
            current_status and current_status.strip().lower() == "executing" and
            current_water is not None and abs(current_water) < 1e-2
        ):
            self.send_type_update(drone_id, "surveillance")
            self.send_status_update(drone_id, "idle")
            self.drone_type[drone_id] = "surveillance"
            self.swap_done = True
            self.get_logger().info(f"{drone_id} water exhausted → role changed to surveillance and status to idle")
            return

        if current_status and current_status.strip().lower() == "surveillance":
            self.send_type_update(drone_id, "irrigation")
            self.drone_type[drone_id] = "irrigation"
            self.swap_done = True
            self.get_logger().info(f"{drone_id} role changed from surveillance to irrigation after mission complete")
            return

    def send_type_update(self, drone_id, new_type):
        msg = DroneTypeChange()
        msg.new_drone_type = new_type
        self.type_update_pubs[drone_id].publish(msg)
        self.get_logger().info(f"Published type update → {drone_id}: {new_type}")

    def send_status_update(self, drone_id, new_status):
        msg = String()
        msg.data = new_status
        self.status_update_pubs[drone_id].publish(msg)
        self.get_logger().info(f"Published status update → {drone_id}: {new_status}")


def main(args=None):
    rclpy.init(args=args)
    node = DynamicRoleSwap()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
