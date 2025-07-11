import rclpy
from rclpy.node import Node

# Import the existing DroneStatus message
from drone_interfaces.msg import DroneStatus
# Import the new custom messages for QGC commands and Mission status
from drone_interfaces.msg import DroneTypeChange, DroneStatusUpdate


class StatusPublisher(Node):

    def __init__(self):
        super().__init__('status_publisher_node')
        self.get_logger().info('StatusPublisher node started for drone_1.')

        # --- Drone State Variables ---
        self.drone_id = 'drone_2'
        self.drone_status = 'idle'       # Initial status
        self.drone_type = 'irrigation' # Initial type

        self.status_publisher = self.create_publisher(
            DroneStatus,
            f'/drone_2/status', # Topic includes drone_id for specificity
            10                                # QoS history depth
        )
        self.get_logger().info(f'Publishing drone status to /drone_2/status.')

        self.qgc_command_subscriber = self.create_subscription(
            DroneTypeChange,
            'drone_2/type_change', # Topic for QGC commands
            self.qgc_command_callback,
            10
        )
        self.get_logger().info('Subscribing to /qgc/command for drone type updates.')

        self.mission_status_subscriber = self.create_subscription(
            DroneStatusUpdate,
            '/drone_2/update_status', # Topic for mission handler status updates
            self.mission_status_callback,
            10
        )
        self.get_logger().info('Subscribing to /mission_handler/status for drone status updates.')
        self.timer = self.create_timer(2.0, self.publish_drone_status)
        self.get_logger().info('Status publishing timer initialized.')

    def qgc_command_callback(self, msg):
        old_drone_type = self.drone_type
        self.drone_type = msg.new_drone_type
        self.get_logger().info(f'QGC changed drone_type from "{old_drone_type}" to "{self.drone_type}".')

    def mission_status_callback(self, msg):
        old_drone_status = self.drone_status
        self.drone_status = msg.status
        self.get_logger().info(f'Mission Handler changed drone_status from "{old_drone_status}" to "{self.drone_status}".')

    def publish_drone_status(self):
        status_msg = DroneStatus()
        status_msg.drone_id = self.drone_id
        status_msg.status = self.drone_status
        status_msg.type = self.drone_type

        self.status_publisher.publish(status_msg)
        self.get_logger().info(f'Published DroneStatus: ID="{status_msg.drone_id}", Status="{status_msg.status}", Type="{status_msg.type}"')


def main(args=None):
    rclpy.init(args=args)
    status_publisher_node = StatusPublisher()
    try:
        # Keep the node running, listening for callbacks and publishing on timer
        rclpy.spin(status_publisher_node)
    except KeyboardInterrupt:
        pass # Allow clean exit on Ctrl+C
    finally:
        # Clean up the node and shut down rclpy
        status_publisher_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
