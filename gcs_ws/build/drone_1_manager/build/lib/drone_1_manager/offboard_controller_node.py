import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import OffboardControlMode, TrajectorySetpoint, VehicleCommand, VehicleLocalPosition, VehicleStatus
from geometry_msgs.msg import PoseStamped
from scipy.spatial.transform import Rotation as R  # ✅ Replaces tf_transformations


class OffboardControl(Node):
    STATE_ARMING_OFFBOARD = 0
    STATE_TAKEOFF = 1
    STATE_HOLD_AND_LISTEN = 2
    STATE_MISSION = 3
    STATE_LANDING = 4

    def __init__(self) -> None:
        super().__init__('offboard_controller_node')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.offboard_control_mode_publisher = self.create_publisher(
            OffboardControlMode, '/fmu/in/offboard_control_mode', qos_profile)
        self.trajectory_setpoint_publisher = self.create_publisher(
            TrajectorySetpoint, '/fmu/in/trajectory_setpoint', qos_profile)
        self.vehicle_command_publisher = self.create_publisher(
            VehicleCommand, '/fmu/in/vehicle_command', qos_profile)

        self.vehicle_local_position_subscriber = self.create_subscription(
            VehicleLocalPosition, '/fmu/out/vehicle_local_position', self.vehicle_local_position_callback, qos_profile)
        self.vehicle_status_subscriber = self.create_subscription(
            VehicleStatus, '/fmu/out/vehicle_status', self.vehicle_status_callback, qos_profile)
        self.dynamic_setpoint_subscriber = self.create_subscription(
            PoseStamped, '/offboard_setpoint_pose', self.dynamic_setpoint_callback, 10)

        self.offboard_setpoint_counter = 0
        self.vehicle_local_position = VehicleLocalPosition()
        self.vehicle_status = VehicleStatus()
        self.takeoff_height = -5.0

        self.target_x = 0.0
        self.target_y = 0.0
        self.target_z = self.takeoff_height
        self.target_yaw = 1.57079  # ~90 degrees

        self.current_state = self.STATE_ARMING_OFFBOARD

        self.timer = self.create_timer(0.1, self.timer_callback)

    def vehicle_local_position_callback(self, msg):
        self.vehicle_local_position = msg

    def vehicle_status_callback(self, msg):
        self.vehicle_status = msg

    def dynamic_setpoint_callback(self, msg: PoseStamped):
        if self.current_state in [self.STATE_HOLD_AND_LISTEN, self.STATE_MISSION]:
            self.target_x = msg.pose.position.x
            self.target_y = msg.pose.position.y
            self.target_z = msg.pose.position.z

            orientation_q = msg.pose.orientation
            quaternion = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
            rotation = R.from_quat(quaternion)
            _, _, self.target_yaw = rotation.as_euler('xyz', degrees=False)

            if self.current_state == self.STATE_HOLD_AND_LISTEN:
                self.current_state = self.STATE_MISSION
                self.get_logger().info("Received first dynamic setpoint. Transitioned to MISSION state.")

            self.get_logger().info(
                f"Received dynamic setpoint: Pos=[{self.target_x:.2f}, {self.target_y:.2f}, {self.target_z:.2f}], Yaw={self.target_yaw:.2f} rad")
        else:
            self.get_logger().warn(
                f"Ignoring dynamic setpoint: Vehicle not in correct state. Current state: {self.current_state}")

    def arm(self):
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=1.0)
        self.get_logger().info("Arm command sent")

    def disarm(self):
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=0.0)
        self.get_logger().info("Disarm command sent")

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

    def publish_position_setpoint(self, x: float, y: float, z: float, yaw: float):
        msg = TrajectorySetpoint()
        msg.position = [x, y, z]
        msg.yaw = yaw
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.trajectory_setpoint_publisher.publish(msg)

    def publish_vehicle_command(self, command: int, **params):
        msg = VehicleCommand()
        msg.command = command
        msg.param1 = params.get("param1", 0.0)
        msg.param2 = params.get("param2", 0.0)
        msg.param3 = params.get("param3", 0.0)
        msg.param4 = params.get("param4", 0.0)
        msg.param5 = params.get("param5", 0.0)
        msg.param6 = params.get("param6", 0.0)
        msg.param7 = params.get("param7", 0.0)
        msg.target_system = 1
        msg.target_component = 1
        msg.source_system = 1
        msg.source_component = 1
        msg.from_external = True
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vehicle_command_publisher.publish(msg)

    def timer_callback(self):
        self.publish_offboard_control_heartbeat_signal()

        if self.current_state == self.STATE_ARMING_OFFBOARD:
            if self.offboard_setpoint_counter < 10:
                self.publish_position_setpoint(0.0, 0.0, self.takeoff_height, self.target_yaw)
                self.offboard_setpoint_counter += 1
            else:
                self.engage_offboard_mode()
                self.arm()
                self.current_state = self.STATE_TAKEOFF
                self.get_logger().info("Transitioned to TAKEOFF state.")
                self.target_x = 0.0
                self.target_y = 0.0
                self.target_z = self.takeoff_height

        elif self.current_state == self.STATE_TAKEOFF:
            self.publish_position_setpoint(0.0, 0.0, self.takeoff_height, self.target_yaw)

            if abs(self.vehicle_local_position.z - self.takeoff_height) < 0.2:
                self.get_logger().info(f"Reached takeoff height. Holding position.")
                self.current_state = self.STATE_HOLD_AND_LISTEN
                self.target_x = self.vehicle_local_position.x
                self.target_y = self.vehicle_local_position.y
                self.target_z = self.vehicle_local_position.z
                self.get_logger().info("Transitioned to HOLD_AND_LISTEN state.")

        elif self.current_state == self.STATE_HOLD_AND_LISTEN:
            self.publish_position_setpoint(self.target_x, self.target_y, self.target_z, self.target_yaw)

        elif self.current_state == self.STATE_MISSION:
            self.publish_position_setpoint(self.target_x, self.target_y, self.target_z, self.target_yaw)

            if self.target_z > -0.5 and abs(self.vehicle_local_position.z) < 1.0:
                self.get_logger().info("Target Z near ground. Initiating landing.")
                self.current_state = self.STATE_LANDING

        elif self.current_state == self.STATE_LANDING:
            self.land()


def main(args=None):
    print("Starting offboard control node with dynamic setpoints...")
    rclpy.init(args=args)
    node = OffboardControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

