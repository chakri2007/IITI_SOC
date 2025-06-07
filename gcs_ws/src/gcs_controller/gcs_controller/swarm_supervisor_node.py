import rclpy
from rclpy.node import Node
from drone_interfaces.msg import DroneStatus, WaypointRequest


class SwarmSupervisorNode(Node):

    def __init__(self):
        super().__init__('swarm_supervisor_node')
        self.get_logger().info("Swarm Supervisor Node Started.")

        # Store latest drone status
        self.drone_status = {}

        # Subscriptions
        self.create_subscription(
            DroneStatus,
            '/drone_1/status',
            self.status_callback,
            10
        )
        self.create_subscription(
            DroneStatus,
            '/drone_2/status',
            self.status_callback,
            10
        )

        # Publishers
        self.waypoint_pub = self.create_publisher(
            WaypointRequest,
            '/waypoint_manager/request',
            10
        )
        self.geotag_pub = self.create_publisher(
            WaypointRequest,
            '/geotag_manager/request',
            10
        )

        self.dispatched = set()

    def status_callback(self, msg: DroneStatus):
        self.drone_status[msg.drone_id] = msg
        self.get_logger().info(f"Status received from {msg.drone_id}")

        drone_type = msg.type.lower()
        drone_status = msg.status.lower()

        if drone_status != 'idle' or drone_type not in ['surveillance', 'irrigation']:
            return

        if msg.drone_id in self.dispatched:
            return

        other_id = 'drone_2' if msg.drone_id == 'drone_1' else 'drone_1'
        direction = msg.direction

        if other_id in self.drone_status:
            other = self.drone_status[other_id]
            other_type = other.drone_type.lower()

            if other_type == drone_type:
                # Same type → split top/bottom
                direction = 'bottom' if other.direction.lower() == 'top' else 'top'
                self.send_request(drone_type, msg.drone_id, direction)
            else:
                # Different types → send both with their own direction
                self.send_request(drone_type, msg.drone_id, msg.direction)
                self.send_request(other_type, other.drone_id, other.direction)

                # Mark both as dispatched
                self.dispatched.add(other.drone_id)

        else:
            # Only one drone known → send request normally
            self.send_request(drone_type, msg.drone_id, direction)

        self.dispatched.add(msg.drone_id)

    def send_request(self, drone_type: str, drone_id: str, direction: str):
        req = WaypointRequest()
        req.drone_id = drone_id
        req.direction = direction

        if drone_type == 'surveillance':
            self.get_logger().info(f"[{drone_id}] → Sending to /waypoint_manager/request from {direction}")
            self.waypoint_pub.publish(req)
        elif drone_type == 'irrigation':
            self.get_logger().info(f"[{drone_id}] → Sending to /geotag_manager/request from {direction}")
            self.geotag_pub.publish(req)
        else:
            self.get_logger().warn(f"Unknown drone type '{drone_type}' for {drone_id}, skipping request.")


def main(args=None):
    rclpy.init(args=args)
    node = SwarmSupervisorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
