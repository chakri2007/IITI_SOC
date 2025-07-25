import math
import rclpy
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from rclpy.node import Node
from px4_msgs.msg import VehicleOdometry, BatteryStatus
from drone_interfaces.msg import DroneStatusUpdate
from geometry_msgs.msg import PoseStamped
import os


class DroneNode(Node):
    def __init__(self):
        super().__init__('drone_node')

        self.declare_parameter('drone_id', 'drone_1')
        self.drone_id = self.get_parameter('drone_id').get_parameter_value().string_value

        self.speed = 2.5
        self.battery = 1.0
        self.position = (0.0, 0.0)
        self.base_position = (0.0, 0.0)  # Set base position to origin
        self.get_logger().info(f"[{self.drone_id}] Base position set to: {self.base_position}")
        
        self.last_working_position = None
        self.reach_threshold = 0.5
        self.status = 'idle'
        self.time = 0
        self.charging_duration = 5
        self.charging_start_time = None
        self.recharge_history = []

        self.fixed_drain_rate = 1.0 / 220.0

        self.status_publisher = self.create_publisher(DroneStatusUpdate, f'/{self.drone_id}/update_status', 10)
        self.setpoint_pub = self.create_publisher(PoseStamped, f'/{self.drone_id}/offboard_setpoint_pose', 10)

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.create_subscription(VehicleOdometry, '/px4_1/fmu/out/vehicle_odometry', self.odometry_callback, qos_profile)
        self.create_subscription(BatteryStatus, '/px4_1/fmu/out/battery_status', self.battery_callback, qos_profile)

        self.timer = self.create_timer(1.0, self.update_logic)

    def write_simulated_battery_percentage(self, percentage):
        try:
            with open("/tmp/sim_voltage0.txt", "w") as f:
                f.write(f"{percentage:.3f}")
        except Exception as e:
            self.get_logger().error(f"Failed to write battery % to file: {e}")

    def odometry_callback(self, msg):
        self.position = (float(msg.position[0]), float(msg.position[1]))

    def battery_callback(self, msg):
        self.battery = msg.remaining

    def update_logic(self):
        self.time += 1

        if self.status == 'idle':
            if should_return_to_base(self.battery, self.distance_to(self.base_position), self.fixed_drain_rate, self.speed):
                self.last_working_position = self.position
                self.status = 'RTL'
                self.send_status('RTL')

        elif self.status == 'RTL':
            self.publish_position_target(self.base_position)
            if self.distance_to(self.base_position) <= self.reach_threshold:
                self.status = 'charging'
                self.charging_start_time = self.time
                self.send_status('charging')

        elif self.status == 'charging':
            elapsed = self.time - self.charging_start_time
            charge_progress = min(1.0, elapsed / self.charging_duration)
            self.write_simulated_battery_percentage(charge_progress)

            if charge_progress >= 1.0:
                self.battery = 1.0
                self.publish_full_battery()
                self.recharge_history.append(self.time)

                try:
                    os.remove("/tmp/sim_voltage0.txt")
                except Exception:
                    pass

                self.status = 'charged'
                self.send_status('charged')


    def publish_position_target(self, target):
        if not target or not isinstance(target[0], (float, int)) or not isinstance(target[1], (float, int)):
            self.get_logger().warn(f"[{self.drone_id}] Invalid position target: {target}")
            return

        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = "map"
        pose.pose.position.x = float(target[0])
        pose.pose.position.y = float(target[1])
        pose.pose.position.z = 2.0
        self.setpoint_pub.publish(pose)

    def distance_to(self, target):
        return math.hypot(self.position[0] - target[0], self.position[1] - target[1])

    def send_status(self, status):
        msg = DroneStatusUpdate()
        msg.drone_id = self.drone_id
        msg.status = status
        self.status_publisher.publish(msg)
        self.get_logger().info(f"[{self.drone_id}] Status: {status}")

    def publish_full_battery(self):
        self.get_logger().info(f"[{self.drone_id}] Battery fully charged.")
        # Additional full battery behavior can go here


def should_return_to_base(battery_level, distance_from_base, drain_rate, speed, safety_margin=0.05):
    time_to_base = distance_from_base / speed
    required_battery = time_to_base * drain_rate
    return battery_level <= (required_battery + safety_margin)


def main(args=None):
    rclpy.init(args=args)
    node = DroneNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
