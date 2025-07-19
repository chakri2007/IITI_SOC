import rclpy
from rclpy.node import Node
from drone_interfaces.msg import DroneStatus, WaypointRequest, GeotagRequest


class SwarmSupervisorNode(Node):
    def __init__(self):
        super().__init__('swarm_supervisor_node')
        self.get_logger().info("Swarm Supervisor Node Started.")

        # Track latest status messages
        self.drone_status = {
            'drone_1': None,
            'drone_2': None
        }

        # Store assigned directions
        self.directions = {
            'drone_1': None,
            'drone_2': None
        }

        # Publishers
        self.waypoint_pub = self.create_publisher(WaypointRequest, '/waypoint_manager/request', 10)
        self.geotag_pub = self.create_publisher(GeotagRequest, '/geotag_manager/request', 10)

        # Subscriptions
        self.create_subscription(DroneStatus, '/drone_1/status', self.status_callback, 10)
        self.create_subscription(DroneStatus, '/drone_2/status', self.status_callback, 10)

    def status_callback(self, msg: DroneStatus):
        drone_id = msg.drone_id
        other_id = 'drone_2' if drone_id == 'drone_1' else 'drone_1'

        drone_type = msg.type.lower().strip()
        status = msg.status.lower().strip()

        self.get_logger().info(f"[{drone_id}] status: {status}, type: {drone_type}")

        # Store latest status
        self.drone_status[drone_id] = msg

        if status != 'idle':
            return

        # Determine safe direction to assign
        other_msg = self.drone_status.get(other_id)
        other_type = other_msg.type.lower().strip() if other_msg else None
        other_direction = self.directions.get(other_id)

        # Conflict prevention: if same type, avoid same direction
        if other_msg and other_type == drone_type:
            direction = 'bottom' if other_direction == 'top' else 'top'
        else:
            direction = 'top'  # default if other is None or different type

        self.directions[drone_id] = direction
        self.send_request(drone_id, drone_type, direction)

    def send_request(self, drone_id: str, drone_type: str, direction: str):
        if drone_type == 'surveillance':
            req = WaypointRequest()
            req.drone_id = drone_id
            req.direction = direction
            self.get_logger().info(f"[{drone_id}] → Sending to /waypoint_manager/request with direction {direction}")
            self.waypoint_pub.publish(req)

        elif drone_type == 'irrigation':
            req = GeotagRequest()
            req.drone_id = drone_id
            req.direction = direction
            self.get_logger().info(f"[{drone_id}] → Sending to /geotag_manager/request with direction {direction}")
            self.geotag_pub.publish(req)

        else:
            self.get_logger().warn(f"Unknown type '{drone_type}' for {drone_id}, skipping request.")


def main(args=None):
    rclpy.init(args=args)
    node = SwarmSupervisorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
