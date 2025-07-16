import rclpy
from rclpy.node import Node
from drone_interfaces.msg import DroneStatus, DroneStatusUpdate


class ChargingQueueNode(Node):
    def __init__(self):
        super().__init__('charging_queue_node')

        self.drone_ids = ['drone_1', 'drone_2']
        self.drone_statuses = {'drone_1': 'idle', 'drone_2': 'idle'}
        self.status_subs = []
        self.status_pubs = {}

        for drone_id in self.drone_ids:
            sub = self.create_subscription(
                DroneStatus,
                f'/{drone_id}/status',
                self.make_status_callback(drone_id),
                10
            )
            self.status_subs.append(sub)

            pub = self.create_publisher(
                DroneStatusUpdate,
                f'/{drone_id}/update_status',
                10
            )
            self.status_pubs[drone_id] = pub

        self.timer = self.create_timer(1.0, self.queue_logic)
        self.get_logger().info("Charging Queue Node initialized.")

    def make_status_callback(self, drone_id):
        def callback(msg):
            if msg.drone_id == drone_id:
                self.drone_statuses[drone_id] = msg.status
        return callback

    def queue_logic(self):
        d1, d2 = self.drone_ids
        s1 = self.drone_statuses[d1].lower()
        s2 = self.drone_statuses[d2].lower()

        # If both in charging state, resolve conflict
        if s1 == 'charging' and s2 == 'charging':
            self.resolve_conflict(d1, d2)

        elif s1 == 'charging' and s2 == 'rtl':
            self.set_hold_to_charge(d2)

        elif s2 == 'charging' and s1 == 'rtl':
            self.set_hold_to_charge(d1)

        # If one was holding and the other is now charged
        if s1 == 'hold_to_charge' and s2 == 'charged':
            self.allow_charging(d1)

        elif s2 == 'hold_to_charge' and s1 == 'charged':
            self.allow_charging(d2)

    def resolve_conflict(self, drone_1, drone_2):
        # Prefer the drone with lexicographically smaller ID
        preferred = min(drone_1, drone_2)
        blocked = drone_2 if preferred == drone_1 else drone_1

        self.set_hold_to_charge(blocked)
        self.get_logger().info(f"[QUEUE] Conflict: {preferred} allowed, {blocked} holding.")

    def set_hold_to_charge(self, drone_id):
        if self.drone_statuses[drone_id] != 'hold_to_charge':
            msg = DroneStatusUpdate()
            msg.drone_id = drone_id
            msg.status = 'hold_to_charge'
            self.status_pubs[drone_id].publish(msg)
            self.get_logger().info(f"[QUEUE] {drone_id} set to hold_to_charge")

    def allow_charging(self, drone_id):
        msg = DroneStatusUpdate()
        msg.drone_id = drone_id
        msg.status = 'charging'
        self.status_pubs[drone_id].publish(msg)
        self.get_logger().info(f"[QUEUE] {drone_id} allowed to charge")


def main(args=None):
    rclpy.init(args=args)
    node = ChargingQueueNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
