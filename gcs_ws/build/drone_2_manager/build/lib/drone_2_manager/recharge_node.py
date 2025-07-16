import math
import rclpy
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from rclpy.node import Node
from px4_msgs.msg import VehicleOdometry, BatteryStatus
from drone_interfaces.msg import DroneStatusUpdate
from geometry_msgs.msg import PoseStamped
import os
from std_msgs.msg import Float32
from drone_interfaces.msg import DroneStatus
from drone_interfaces.msg import SurveillanceStatus



class DroneNode(Node):
    def __init__(self):
        super().__init__('drone_node')

        self.declare_parameter('drone_id', 'drone_2')
        self.drone_id = self.get_parameter('drone_id').get_parameter_value().string_value

        self.speed = 6
        self.battery = 1.0
        self.position = (0.0, 0.0, 0.0)
        self.base_position = (0.0, 0.0)  # Set base position to origin
        self.get_logger().info(f"[{self.drone_id}] Base position set to: {self.base_position}")
        
        self.last_working_position = None
        self.reach_threshold = 5
        self.status = 'idle'
        self.time = 0
        self.charging_duration = 90
        self.charging_start_time = None
        self.recharge_history = []
        self.water_level = 100.0
        self.low_water_threshold = 0.0
        self.recharging_due_to_water = False

        self.fixed_drain_rate = 1.0 / 90.0
        self.has_water_tank = False  # default
        self.drone_type_sub = self.create_subscription(
            DroneStatus,
            f'/{self.drone_id}/status',  # assuming drone_id like 'drone_1'
            self.drone_type_callback,
            10
        )

        self.surveillance_completed = False  # default

        self.create_subscription(
            SurveillanceStatus,
            '/surveillance_status',
            self.surveillance_callback,
            10
        )



        self.status_publisher = self.create_publisher(DroneStatusUpdate, f'/{self.drone_id}/update_status', 10)
        self.setpoint_pub = self.create_publisher(PoseStamped, f'/{self.drone_id}/offboard_setpoint_pose', 10)

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.create_subscription(VehicleOdometry, '/px4_2/fmu/out/vehicle_odometry', self.odometry_callback, qos_profile)
        self.create_subscription(BatteryStatus, '/px4_2/fmu/out/battery_status', self.battery_callback, qos_profile)
        self.create_subscription(Float32, f'/{self.drone_id}/water_level', self.water_callback, 10)

        self.timer = self.create_timer(1.0, self.update_logic)

    def write_simulated_battery_percentage(self, percentage):
        try:
            with open("/tmp/sim_voltage_2.txt", "w") as f:
                f.write(f"{percentage:.3f}")
        except Exception as e:
            self.get_logger().error(f"Failed to write battery % to file: {e}")

    def odometry_callback(self, msg):
        self.position = (float(msg.position[0]), float(msg.position[1]))

    def battery_callback(self, msg):
        self.battery = msg.remaining
        
    def water_callback(self, msg: Float32):
        self.water_level = msg.data

    def surveillance_callback(self, msg):
        self.surveillance_completed = msg.surveillance_completed
        self.get_logger().info(f"[{self.drone_id}] Surveillance status → completed: {msg.surveillance_completed}")

    def drone_type_callback(self, msg):
        if msg.drone_id == self.drone_id:
            if msg.type.lower() == "irrigation":
                self.has_water_tank = True
            else:
                self.has_water_tank = False
            self.get_logger().info(f"Drone type received: {msg.type}, has_water_tank set to {self.has_water_tank}")

            # ✅ Set current status based on external update
            self.status = msg.status.lower().strip()
            self.get_logger().info(f"[{self.drone_id}] Received status update: {self.status}")



    def update_logic(self):
        self.time += 1

        if ((self.status == 'idle') or (self.status == 'executing')):
            battery_low = should_return_to_base(
                self.battery,
                self.distance_to(self.base_position),
                self.fixed_drain_rate,
                self.speed
            )

            water_empty = (
                self.has_water_tank and 
                self.water_level <= self.low_water_threshold and 
                self.surveillance_completed
            )

            if battery_low or water_empty:
                self.last_working_position = self.position
                self.status = 'RTL'
                self.recharging_due_to_water = water_empty
                self.send_status('RTL')

        elif self.status == 'RTL':
            self.publish_position_target(self.base_position)
            if self.distance_to(self.base_position) <= self.reach_threshold:
                self.status = 'charging'
                self.send_status('charging')

        elif self.status == 'charging':
            if self.charging_start_time is None:
                self.get_logger().info(f"[{self.drone_id}] Charging started.")
                self.charging_start_time = self.time  # ✅ Safe initialization

            elapsed = self.time - self.charging_start_time
            charge_progress = min(1.0, elapsed / self.charging_duration)
            self.write_simulated_battery_percentage(charge_progress)

            if charge_progress >= 1.0:
                self.battery = 1.0
                self.publish_full_battery()
                self.recharge_history.append(self.time)

                try:
                    os.remove("/tmp/sim_voltage_1.txt")
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
        pose.pose.position.z = 0.0
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
