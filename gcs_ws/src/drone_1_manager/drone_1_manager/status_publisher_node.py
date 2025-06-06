import rclpy
from rclpy.node import Node

# Import the existing DroneStatus message
from drone_interfaces.msg import DroneStatus
# Import the new custom messages for QGC commands and Mission status
from drone_interfaces.msg import QGCCommand, MissionStatus


class StatusPublisher(Node):
    """
    A ROS 2 node that publishes the current status of a drone,
    including its ID, operational status, and type. It can update
    its status and type based on messages from other nodes.
    """

    def __init__(self):
        super().__init__('status_publisher_node')
        self.get_logger().info('StatusPublisher node started for drone_1.')

        # --- Drone State Variables ---
        self.drone_id = 'drone_1'
        self.drone_status = 'idle'       # Initial status
        self.drone_type = 'surveillance' # Initial type

        # --- Publisher for DroneStatus messages ---
        # This node publishes the current status of drone_1 on a dedicated topic.
        self.status_publisher = self.create_publisher(
            DroneStatus,
            f'/drone/{self.drone_id}/status', # Topic includes drone_id for specificity
            10                                # QoS history depth
        )
        self.get_logger().info(f'Publishing drone status to /drone/{self.drone_id}/status.')

        # --- Subscriber for QGC Commands (to change drone type) ---
        # Listens for commands from a Quality Ground Control (QGC) station to update drone type.
        self.qgc_command_subscriber = self.create_subscription(
            QGCCommand,
            '/qgc/command', # Topic for QGC commands
            self.qgc_command_callback,
            10
        )
        self.get_logger().info('Subscribing to /qgc/command for drone type updates.')

        # --- Subscriber for Mission Handler Status (to change drone status) ---
        # Listens for status updates from a mission handler node to change operational status.
        self.mission_status_subscriber = self.create_subscription(
            MissionStatus,
            '/mission_handler/status', # Topic for mission handler status updates
            self.mission_status_callback,
            10
        )
        self.get_logger().info('Subscribing to /mission_handler/status for drone status updates.')

        # --- Timer for periodic status publishing ---
        # Publishes the current drone status every 2 seconds.
        self.timer = self.create_timer(2.0, self.publish_drone_status)
        self.get_logger().info('Status publishing timer initialized.')

    def qgc_command_callback(self, msg):
        """
        Callback function for QGCCommand messages.
        Updates the drone's type based on the received command.
        """
        old_drone_type = self.drone_type
        self.drone_type = msg.new_drone_type.upper() # Store type in uppercase for consistency
        self.get_logger().info(f'QGC changed drone_type from "{old_drone_type}" to "{self.drone_type}".')

    def mission_status_callback(self, msg):
        """
        Callback function for MissionStatus messages.
        Updates the drone's operational status based on the received message.
        """
        old_drone_status = self.drone_status
        self.drone_status = msg.new_drone_status.upper() # Store status in uppercase
        self.get_logger().info(f'Mission Handler changed drone_status from "{old_drone_status}" to "{self.drone_status}".')

    def publish_drone_status(self):
        """
        Creates and publishes a DroneStatus message with the current
        drone_id, drone_status, and drone_type.
        """
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
