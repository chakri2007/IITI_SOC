import rclpy
from rclpy.node import Node
from drone_interfaces.msg import DroneStatus, WaypointRequest
from rclpy.duration import Duration
from builtin_interfaces.msg import Time


class SwarmSupervisorNode(Node):

    def __init__(self):
        super().__init__('swarm_supervisor_node')
        self.get_logger().info("Swarm Supervisor Node Started.")

        self.drone_status = {}
        self.last_seen = {}
        self.dispatched = set()

        self.timeout_sec = 10.0  # seconds

        # Subscriptions
        self.create_subscription(DroneStatus, '/drone_1/status', self.status_callback, 10)
        self.create_subscription(DroneStatus, '/drone_2/status', self.status_callback, 10)

        # Publishers
        self.waypoint_pub = self.create_publisher(WaypointRequest, '/waypoint_manager/request', 10)
        self.geotag_pub = self.create_publisher(WaypointRequest, '/geotag_manager/request', 10)

        # Timer to check for drone timeouts
        self.create_timer(2.0, self.check_for_unpaired_drones)

    def status_callback(self, msg: DroneStatus):
        now = self.get_clock().now()
        self.drone_status[msg.drone_id] = msg
        self.last_seen[msg.drone_id] = now

        self.get_logger().info(f"Status received from {msg.drone_id}")

        if msg.status.lower() != 'idle' or msg.type.lower() not in ['surveillance', 'irrigation']:
            return

        if msg.drone_id in self.dispatched:
            return

        other_id = 'drone_2' if msg.drone_id == 'drone_1' else 'drone_1'
        direction = msg.direction

        if other_id in self.drone_status:
            other = self.drone_status[other_id]
            if other.type.lower() == msg.type.lower():
                direction = 'bottom' if other.direction.lower() == 'top' else 'top'
                self.send_request(msg.type.lower(), msg.drone_id, direction)
            else:
                self.send_request(msg.type.lower(), msg.drone_id, msg.direction)
                self.send_request(other.type.lower(), other.drone_id, other.direction)
                self.dispatched.add(other.drone_id)

        else:
            # Other drone not seen yet, will handle in timeout timer
            return

        self.dispatched.add(msg.drone_id)

    def check_for_unpaired_drones(self):
        now = self.get_clock().now()
        for drone_id, msg in self.drone_status.items():
            if drone_id in self.dispatched:
                continue

            last_time = self.last_seen.get(drone_id)
            if last_time and (now - last_time) > Duration(seconds=self.timeout_sec):
                other_id = 'drone_2' if drone_id == 'drone_1' else 'drone_1'
                if other_id not in self.drone_status:
                    self.get_logger().warn(f"{other_id} offline or not seen in {self.timeout_sec} sec. Proceeding with {drone_id} alone.")
                    self.send_request(msg.type.lower(), drone_id, msg.direction)
                    self.dispatched.add(drone_id)

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
