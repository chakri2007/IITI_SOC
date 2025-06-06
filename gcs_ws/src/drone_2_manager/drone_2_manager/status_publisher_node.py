# ~/iit_dual_drone_ws/src/drone_2_manager/drone_2_manager/status_publisher_node.py
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from drone_interfaces.msg import DroneStatus # Import DroneStatus
from std_msgs.msg import Header
import time

class StatusPublisherNode(Node):
    def __init__(self):
        super().__init__('drone_2_status_publisher_node')

        self.drone_id = 2
        self.get_logger().info(f'StatusPublisherNode initialized for Drone ID: {self.drone_id}')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.status_publisher = self.create_publisher(
            DroneStatus,
            f'/drone/drone_2/status',
            qos_profile
        )

        # Initial simulated drone state for Irrigation Drone (Drone 2)
        self.battery_percentage = 100.0
        self.water_percentage = 100.0 # Irrigation drone, tank is full
        self.current_task = DroneStatus.IDLE
        self.last_visited_waypoint_id = 0
        self.drone_type = DroneStatus.TYPE_IRRIGATION # Set drone type here

        self.timer = self.create_timer(1.0, self.publish_status)
        self.get_logger().info('Drone 2 Status Publisher Node started as Irrigation Drone (constant resources).')

    def publish_status(self):
        """Publishes the current simulated status of Drone 2."""
        msg = DroneStatus()
        msg.header = Header(stamp=self.get_clock().now().to_msg())
        msg.drone_id = self.drone_id
        msg.battery_percentage = self.battery_percentage
        msg.water_percentage = self.water_percentage
        msg.current_task = self.current_task
        msg.last_visited_waypoint_id = self.last_visited_waypoint_id
        msg.drone_type = self.drone_type # Publish the drone type

        self.status_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()