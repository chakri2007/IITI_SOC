import rclpy
from rclpy.node import Node
import json
from drone_interfaces.msg import SurveillanceStatus  

class SurveillanceMonitorNode(Node):
    def __init__(self):
        super().__init__('surveillance_monitor_node')
        self.publisher_ = self.create_publisher(SurveillanceStatus, 'surveillance_status', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Declare parameter for JSON file path
        self.declare_parameter('waypoint_file_path', '')
        self.json_file_path = self.get_parameter('json_file_path').get_parameter_value().string_value

    def timer_callback(self):
        try:
            with open(self.json_file_path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            self.get_logger().error(f"Error reading JSON: {e}")
            return

        remaining = sum(1 for p in data if not p.get('visited', False))
        completed = (remaining == 0)

        msg = SurveillanceStatus()
        msg.surveillance_completed = completed
        msg.waypoints_remaining = remaining

        self.publisher_.publish(msg)
        self.get_logger().info(f"Published → completed={completed}, remaining={remaining}")

def main(args=None):
    rclpy.init(args=args)
    node = SurveillanceMonitorNode()
    rclpy.spin(node)
    rclpy.shutdown()
