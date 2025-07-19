#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import (
    OffboardControlMode,
    TrajectorySetpoint,
    VehicleCommand,
    VehicleLocalPosition,
    VehicleStatus,
    VehicleOdometry,
    VehicleCommandAck,
    VehicleLandDetected
)
from geometry_msgs.msg import PoseStamped
from drone_interfaces.msg import DroneStatusUpdate, DroneStatus
import numpy as np


def quaternion_to_yaw(qx, qy, qz, qw):
    numerator = 2.0 * (qx * qy + qw * qz)
    denominator = qw * qw + qx * qx - qy * qy - qz * qz
    return float(np.arctan2(numerator, denominator))


class OffboardControl(Node):

    def __init__(self) -> None:
        super().__init__('offboard_control_node')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # Publishers
        self.offboard_control_mode_publisher = self.create_publisher(
            OffboardControlMode, '/px4_2/fmu/in/offboard_control_mode', qos_profile)
        self.trajectory_setpoint_publisher = self.create_publisher(
            TrajectorySetpoint, '/px4_2/fmu/in/trajectory_setpoint', qos_profile)
        self.vehicle_command_publisher = self.create_publisher(
            VehicleCommand, '/px4_2/fmu/in/vehicle_command', qos_profile)
        self.mission_status_publisher = self.create_publisher(
            DroneStatusUpdate, '/drone_2/update_status', 10
        )

        # Subscriptions
        self.create_subscription(
            VehicleLocalPosition, '/px4_2/fmu/out/vehicle_local_position', self.vehicle_local_position_callback, qos_profile)
        self.create_subscription(
            VehicleStatus, '/px4_2/fmu/out/vehicle_status', self.vehicle_status_callback, qos_profile)
        self.create_subscription(
            VehicleOdometry, '/px4_2/fmu/out/vehicle_odometry', self.vehicle_odometry_callback, qos_profile)
        self.create_subscription(
            VehicleCommandAck, '/px4_2/fmu/out/vehicle_command_ack', self.vehicle_command_ack_callback, qos_profile)
        self.create_subscription(
            VehicleLandDetected, '/px4_2/fmu/out/vehicle_land_detected', self.vehicle_land_detected_callback, qos_profile)
        self.create_subscription(
            PoseStamped, '/drone_2/offboard_setpoint_pose', self.dynamic_waypoint_callback, 10)
        self.mission_status_subscriber = self.create_subscription(
            DroneStatus, '/drone_2/status', self.mission_status_callback, 10)

        # State holders
        self.vehicle_local_position = VehicleLocalPosition()
        self.vehicle_status = VehicleStatus()
        self.vehicle_odometry = VehicleOdometry()
        self.vehicle_command_ack = VehicleCommandAck()
        self.vehicle_land_detected = VehicleLandDetected()

        self.takeoff_height = -30.0
        self.offboard_setpoint_counter = 0
        self.taken_off = False

        self.current_dynamic_pose = None
        self.tracking_dynamic_waypoint = False
        self.status_updated = False
        self.current_status = ""

        # Timer
        self.timer = self.create_timer(0.1, self.timer_callback)

    # ========== Callbacks ==========

    def vehicle_local_position_callback(self, msg):
        self.vehicle_local_position = msg

    def vehicle_status_callback(self, msg):
        self.vehicle_status = msg

    def vehicle_odometry_callback(self, msg):
        self.vehicle_odometry = msg

    def vehicle_command_ack_callback(self, msg):
        self.vehicle_command_ack = msg

    def vehicle_land_detected_callback(self, msg):
        self.vehicle_land_detected = msg

    def dynamic_waypoint_callback(self, msg: PoseStamped):
        if self.taken_off:
            self.current_dynamic_pose = msg
            self.tracking_dynamic_waypoint = True
            self.get_logger().info(
                f"Received dynamic waypoint: ({msg.pose.position.x}, {msg.pose.position.y}, {msg.pose.position.z})"
            )

    def mission_status_callback(self, msg: DroneStatus):
        status = msg.status.lower().strip()
        self.current_status = status
        self.get_logger().info(f"Received mission status node 1: {status}")

        if status == "charging":
            self.land()
            self.offboard_setpoint_counter = 11
            self.taken_off = False
            self.status_updated = False
            self.get_logger().info("Drone is charging. Sent LAND command. Will disarm after landing.")

        elif status == "charged":
            self.status_updated = True
            self.taken_off = False   # ✅ Add this
            self.offboard_setpoint_counter = 0
            self.get_logger().info("Drone is charged. Will initiate takeoff.")

    # ========== Publishing helpers ==========

    def publish_status(self, new_status: str):
        msg = DroneStatusUpdate()
        msg.drone_id = "drone_2"
        msg.status = new_status
        self.mission_status_publisher.publish(msg)
        self.get_logger().info(f"Published drone status: {new_status}")

    def arm(self):
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=1.0)
        self.get_logger().info('Arm command sent')

    def disarm(self):
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=0.0)
        self.get_logger().info('Disarm command sent')

    def engage_offboard_mode(self):
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_DO_SET_MODE, param1=1.0, param2=6.0)
        self.get_logger().info("Switching to offboard mode")

    def land(self):
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_NAV_LAND)
        self.get_logger().info("Switching to land mode")

    def publish_offboard_control_heartbeat_signal(self):
        msg = OffboardControlMode()
        msg.position = True
        msg.velocity = False
        msg.acceleration = False
        msg.attitude = False
        msg.body_rate = False
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.offboard_control_mode_publisher.publish(msg)

    def publish_position_setpoint(self, x: float, y: float, z: float, yaw: float = 1.57079):
        msg = TrajectorySetpoint()
        msg.position = [x, y, z]
        msg.yaw = yaw
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.trajectory_setpoint_publisher.publish(msg)

    def publish_vehicle_command(self, command, **params):
        msg = VehicleCommand()
        msg.command = command
        msg.param1 = params.get("param1", 0.0)
        msg.param2 = params.get("param2", 0.0)
        msg.param3 = params.get("param3", 0.0)
        msg.param4 = params.get("param4", 0.0)
        msg.param5 = params.get("param5", 0.0)
        msg.param6 = params.get("param6", 0.0)
        msg.param7 = params.get("param7", 0.0)
        msg.target_system = 0
        msg.target_component = 1
        msg.source_system = 1
        msg.source_component = 1
        msg.from_external = True
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vehicle_command_publisher.publish(msg)

    def compute_yaw_from_odometry(self):
        q = self.vehicle_odometry.q
        return quaternion_to_yaw(q[0], q[1], q[2], q[3])

    # ========== Timer ==========

    def timer_callback(self):
        self.publish_offboard_control_heartbeat_signal()

        if self.current_status == "charging":
         return

        if self.offboard_setpoint_counter == 10:
            self.engage_offboard_mode()
            self.arm()

        # Handle takeoff after "charged" status
        if not self.taken_off:
            self.publish_position_setpoint(0.0, 0.0, self.takeoff_height)

        # Confirm takeoff and publish idle
        if (self.vehicle_local_position.z > self.takeoff_height and
            self.vehicle_status.nav_state == VehicleStatus.NAVIGATION_STATE_OFFBOARD and
            not self.taken_off):
            if self.vehicle_local_position.z < self.takeoff_height + 0.5:
                self.taken_off = True
                self.status_updated = False
                self.publish_status("idle")
                self.get_logger().info("Takeoff complete. Status set to idle.")

        # Track waypoint after takeoff
        if self.taken_off and self.tracking_dynamic_waypoint and self.current_dynamic_pose:
            x = self.current_dynamic_pose.pose.position.x
            y = self.current_dynamic_pose.pose.position.y
            z = self.current_dynamic_pose.pose.position.z
            yaw = self.compute_yaw_from_odometry()
            self.publish_position_setpoint(x, y, z, yaw)

        # Automatically disarm once landed during charging
        if (self.current_status == "charging" and
            self.vehicle_land_detected.landed and
            self.vehicle_status.arming_state != VehicleStatus.ARMING_STATE_DISARMED):
            self.get_logger().info("Detected landed. Sending disarm.")
            self.disarm()

        if self.offboard_setpoint_counter < 11:
            self.offboard_setpoint_counter += 1


# ========== Main ==========

def main(args=None):
    print('Starting offboard control node...')
    rclpy.init(args=args)
    node = OffboardControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
