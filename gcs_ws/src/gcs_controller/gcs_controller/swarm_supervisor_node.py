import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from drone_interfaces.msg import DroneStatus, WaypointRequest, GeotagRequest


class SwarmSupervisorNode(Node):

    def __init__(self):
        super().__init__('swarm_supervisor_node')
        self.get_logger().info("Swarm Supervisor Node Started.")

        self.drone_status = {}
        self.last_seen = {}
        self.actively_dispatched = set()
        self.assigned_direction = {}   # NEW: track the direction per drone
        self.timeout_sec = 10.0

        # Subscriptions
        self.create_subscription(DroneStatus, '/drone_1/status', self.status_callback, 10)
        self.create_subscription(DroneStatus, '/drone_2/status', self.status_callback, 10)

        # Publishers
        self.waypoint_pub = self.create_publisher(WaypointRequest, '/waypoint_manager/request', 10)
        self.geotag_pub = self.create_publisher(GeotagRequest, '/geotag_manager/request', 10)

        # Timer
        self.create_timer(2.0, self.check_for_unpaired_drones)

    def status_callback(self, msg: DroneStatus):
        now = self.get_clock().now()

        drone_id = msg.drone_id
        drone_type = msg.type.lower().strip()
        drone_status = msg.status.lower().strip()

        # Ignore direction from the drone
        self.get_logger().info(f"[{drone_id}] status: {drone_status}, type: {drone_type}")

        self.drone_status[drone_id] = msg
        self.last_seen[drone_id] = now

        if drone_status == 'idle' and drone_id in self.actively_dispatched:
            self.get_logger().info(f"[{drone_id}] is now idle. Removing from actively_dispatched set.")
            self.actively_dispatched.remove(drone_id)

        if drone_status != 'idle' or drone_type not in ['surveillance', 'irrigation'] or drone_id in self.actively_dispatched:
            return

        other_id = 'drone_2' if drone_id == 'drone_1' else 'drone_1'

        if other_id in self.drone_status and other_id not in self.actively_dispatched:
            other = self.drone_status[other_id]
            other_type = other.type.lower().strip()
            other_status = other.status.lower().strip()

            if other_status == 'idle' and other_type in ['surveillance', 'irrigation']:
                if other_type == drone_type:
                    # SAME TYPE → assign different directions
                    other_direction = self.assigned_direction.get(other_id, 'top')
                    new_direction = 'bottom' if other_direction == 'top' else 'top'

                    self.assign_and_send(drone_type, drone_id, new_direction)
                    self.assign_and_send(other_type, other_id, other_direction)

                else:
                    # DIFFERENT TYPES → assign same direction
                    direction = 'top'
                    self.assign_and_send(drone_type, drone_id, direction)
                    self.assign_and_send(other_type, other_id, direction)

                self.actively_dispatched.add(drone_id)
                self.actively_dispatched.add(other_id)

            else:
                self.get_logger().info(f"{other_id} is not idle or already dispatched. Waiting for timeout...")
        else:
            self.get_logger().info(f"{other_id} not yet active or already dispatched. Waiting for timeout...")

    def check_for_unpaired_drones(self):
        now = self.get_clock().now()
        self.get_logger().info("Checking for unpaired drones...")

        for drone_id in list(self.drone_status.keys()):
            if drone_id in self.actively_dispatched:
                continue

            msg = self.drone_status[drone_id]
            last_seen = self.last_seen.get(drone_id)

            if msg.status.lower().strip() != 'idle':
                continue

            if not last_seen:
                continue

            other_id = 'drone_2' if drone_id == 'drone_1' else 'drone_1'
            other_last_seen = self.last_seen.get(other_id)

            other_is_active = other_id in self.drone_status and \
                              (other_last_seen and (now - other_last_seen) <= Duration(seconds=self.timeout_sec))

            if not other_is_active or (other_id in self.actively_dispatched):
                # Use assigned or default direction
                direction = self.assigned_direction.get(drone_id, 'top')
                self.get_logger().warn(f"{other_id} is offline, timed out (> {self.timeout_sec}s), or actively dispatched. Dispatching {drone_id} solo.")
                self.assign_and_send(msg.type.lower().strip(), drone_id, direction)
                self.actively_dispatched.add(drone_id)
            else:
                self.get_logger().info(f"{drone_id} is active and idle, and {other_id} is also active and idle. Waiting for pair.")

    def assign_and_send(self, drone_type: str, drone_id: str, direction: str):
        # Store the assigned direction internally
        self.assigned_direction[drone_id] = direction

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
            self.get_logger().warn(f"Unknown drone type '{drone_type}' for {drone_id}, skipping request.")


def main(args=None):
    rclpy.init(args=args)
    node = SwarmSupervisorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()