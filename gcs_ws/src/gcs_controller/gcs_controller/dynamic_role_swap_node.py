import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from drone_interfaces.msg import DroneTypeChange  
from drone_interfaces.msg import SurveillanceStatus

class DynamicRoleSwap(Node):
    def __init__(self):
        super().__init__('dynamic_role_swap_node')

        self.swap_done = False
        self.subscribed = False

        self.drone_status = {
            "drone_1": None,
            "drone_2": None
        }

        self.type_update_pubs = {
            "drone_1": self.create_publisher(DroneTypeChange, 'drone_1/type_change', 10),
            "drone_2": self.create_publisher(DroneTypeChange, 'drone_2/type_change', 10)
        }

        # Subscribe to surveillance monitor node's status
        self.create_subscription(
            SurveillanceStatus,
            'surveillance_status',
            self.surveillance_status_callback,
            10
        )

    def surveillance_status_callback(self, msg: SurveillanceStatus):
        if self.swap_done or self.subscribed:
            return

        if msg.surveillance_completed:
            self.get_logger().info("Surveillance complete. Subscribing to drone status...")
            self.subscribe_to_status()

    def subscribe_to_status(self):
        self.sub_1 = self.create_subscription(String, 'drone_1/status', self.status_callback_1, 10)
        self.sub_2 = self.create_subscription(String, 'drone_2/status', self.status_callback_2, 10)
        self.subscribed = True

    def status_callback_1(self, msg):
        self.drone_status["drone_1"] = msg.data
        self.check_and_swap()

    def status_callback_2(self, msg):
        self.drone_status["drone_2"] = msg.data
        self.check_and_swap()

    def check_and_swap(self):
        if self.swap_done:
            return

        for drone_id, status in self.drone_status.items():
            if status == "surveillance":
                self.send_type_update(drone_id, "irrigation")
                self.swap_done = True
                self.get_logger().info(f"Swapped role for {drone_id} to 'irrigation'")
                break

    def send_type_update(self, drone_id, new_type):
        msg = DroneTypeChange()
        msg.new_drone_type = new_type
        self.type_update_pubs[drone_id].publish(msg)
        self.get_logger().info(f"Published type update to {drone_id}: {new_type}")

def main(args=None):
    rclpy.init(args=args)
    node = DynamicRoleSwap()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
