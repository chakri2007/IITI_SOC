
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import OffboardControlMode, TrajectorySetpoint, VehicleCommand, VehicleLocalPosition, VehicleStatus
from geometry_msgs.msg import PoseStamped  # Import for dynamic setpoints
from tf_transformations import euler_from_quaternion  # Import for extracting yaw from quaternion


class OffboardControl(Node):
    """Node for controlling a vehicle in offboard mode with dynamic setpoints."""

    # Define states for the vehicle's operation to manage flight phases
    STATE_ARMING_OFFBOARD = 0    # Initial state: sending heartbeats, arming, engaging offboard
    STATE_TAKEOFF = 1            # Climbing to the desired takeoff height
    STATE_HOLD_AND_LISTEN = 2    # Holding position after takeoff, awaiting first dynamic command
    STATE_MISSION = 3            # Actively following dynamic setpoints
    STATE_LANDING = 4            # Initiating and performing the landing sequence

    def __init__(self) -> None:
        """
        Initializes the OffboardControl node.
        Sets up publishers, subscribers, QoS profiles, and initializes state variables.
        """
        super().__init__('offboard_controller_node')

        # Configure QoS profile for publishing and subscribing to PX4 topics
        # BEST_EFFORT: for real-time data, doesn't guarantee delivery but prioritizes latest data
        # TRANSIENT_LOCAL: keeps the last message for new subscribers (important for latching states)
        # KEEP_LAST: keeps only the latest message
        # depth=1: only one message in the history buffer
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # Create publishers for sending commands to PX4
        # offboard_control_mode: publishes heartbeat signal to maintain offboard mode
        self.offboard_control_mode_publisher = self.create_publisher(
            OffboardControlMode, '/fmu/in/offboard_control_mode', qos_profile)
        # trajectory_setpoint: publishes desired position and yaw
        self.trajectory_setpoint_publisher = self.create_publisher(
            TrajectorySetpoint, '/fmu/in/trajectory_setpoint', qos_profile)
        # vehicle_command: publishes various commands like arm, disarm, engage offboard, land
        self.vehicle_command_publisher = self.create_publisher(
            VehicleCommand, '/fmu/in/vehicle_command', qos_profile)

        # Create subscribers for receiving feedback from PX4
        # vehicle_local_position: provides current position (x, y, z) in NED frame
        self.vehicle_local_position_subscriber = self.create_subscription(
            VehicleLocalPosition, '/fmu/out/vehicle_local_position', self.vehicle_local_position_callback, qos_profile)
        # vehicle_status: provides current vehicle state (armed, disarmed, nav_state, etc.)
        self.vehicle_status_subscriber = self.create_subscription(
            VehicleStatus, '/fmu/out/vehicle_status', self.vehicle_status_callback, qos_profile)

        # NEW: Subscriber for dynamic setpoints (from another ROS 2 node)
        # This topic will receive PoseStamped messages, which contain position and orientation (quaternion)
        # The position (x,y,z) and orientation (from which yaw is derived) will be used as dynamic targets.
        self.dynamic_setpoint_subscriber = self.create_subscription(
            PoseStamped, '/offboard_setpoint_pose', self.dynamic_setpoint_callback, qos_profile)

        # Initialize variables for vehicle state and control
        self.offboard_setpoint_counter = 0  # Counter for initial offboard engagement and arming sequence
        self.vehicle_local_position = VehicleLocalPosition()  # Store latest local position
        self.vehicle_status = VehicleStatus()                # Store latest vehicle status
        self.takeoff_height = -5.0  # Desired takeoff altitude in meters (negative Z in NED convention for upward)

        # Initialize dynamic setpoint variables
        # These will be updated by the dynamic_setpoint_callback
        self.target_x = 0.0
        self.target_y = 0.0
        self.target_z = self.takeoff_height  # Initially set to takeoff height
        self.target_yaw = 1.57079  # Default yaw (90 degrees in radians)

        # Initialize the state machine
        self.current_state = self.STATE_ARMING_OFFBOARD

        # Create a timer to regularly publish control commands and check state
        # The timer callback will be executed every 0.1 seconds (10 Hz)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def vehicle_local_position_callback(self, vehicle_local_position: VehicleLocalPosition) -> None:
        """Callback function for vehicle_local_position topic subscriber.
        Updates the stored local position of the vehicle."""
        self.vehicle_local_position = vehicle_local_position

    def vehicle_status_callback(self, vehicle_status: VehicleStatus) -> None:
        """Callback function for vehicle_status topic subscriber.
        Updates the stored status of the vehicle."""
        self.vehicle_status = vehicle_status

    def dynamic_setpoint_callback(self, msg: PoseStamped) -> None:
        """
        NEW: Callback function for dynamic setpoint (PoseStamped) messages.
        This function is triggered when a new PoseStamped message is received on `/offboard_setpoint_pose`.
        It updates the internal target position (x, y, z) and yaw from the received message.
        """
        # Only update target if the vehicle is in a state where it should be following missions
        if self.current_state == self.STATE_HOLD_AND_LISTEN or \
           self.current_state == self.STATE_MISSION:
            self.target_x = msg.pose.position.x
            self.target_y = msg.pose.position.y
            self.target_z = msg.pose.position.z  # Assuming Z is already in NED convention (negative for upward)

            # Extract yaw from the quaternion (orientation) in the PoseStamped message
            # The euler_from_quaternion function returns (roll, pitch, yaw)
            orientation_q = msg.pose.orientation
            quaternion = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
            _, _, self.target_yaw = euler_from_quaternion(quaternion)

            # If currently holding, transition to mission state upon receiving the first dynamic setpoint
            if self.current_state == self.STATE_HOLD_AND_LISTEN:
                self.current_state = self.STATE_MISSION
                self.get_logger().info("Received first dynamic setpoint. Transitioned to MISSION state.")

            self.get_logger().info(f"Received dynamic setpoint: Pos=[{self.target_x:.2f}, {self.target_y:.2f}, {self.target_z:.2f}], Yaw={self.target_yaw:.2f} rad")
        else:
            self.get_logger().warn(
                f"Ignoring dynamic setpoint: Vehicle not in HOLD_AND_LISTEN or MISSION state. Current state: {self.current_state}")

    def arm(self) -> None:
        """Send an arm command to the vehicle."""
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=1.0)  # param1=1.0 for ARM
        self.get_logger().info('Arm command sent')

    def disarm(self) -> None:
        """Send a disarm command to the vehicle."""
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1=0.0)  # param1=0.0 for DISARM
        self.get_logger().info('Disarm command sent')

    def engage_offboard_mode(self) -> None:
        """Send a command to switch the vehicle to offboard mode."""
        # param1=1.0: PX4_CUSTOM_MAIN_MODE_OFFBOARD
        # param2=6.0: PX4_CUSTOM_SUB_MODE_OFFBOARD_STABILIZED (specific sub-mode for position control)
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_DO_SET_MODE, param1=1.0, param2=6.0)
        self.get_logger().info("Switching to offboard mode")

    def land(self) -> None:
        """Send a command to switch the vehicle to land mode."""
        self.publish_vehicle_command(VehicleCommand.VEHICLE_CMD_NAV_LAND)
        self.get_logger().info("Switching to land mode")

    def publish_offboard_control_heartbeat_signal(self) -> None:
        """
        Publishes the OffboardControlMode message.
        This "heartbeat" is crucial to maintain offboard mode; if not sent regularly,
        the vehicle will exit offboard mode.
        Sets position control to True, others to False for position control.
        """
        msg = OffboardControlMode()
        msg.position = True       # Enable position control
        msg.velocity = False
        msg.acceleration = False
        msg.attitude = False
        msg.body_rate = False
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.offboard_control_mode_publisher.publish(msg)

    def publish_position_setpoint(self, x: float, y: float, z: float, yaw: float) -> None:
        """
        Publishes a TrajectorySetpoint message with the desired position and yaw.
        Args:
            x (float): Desired X position in NED frame.
            y (float): Desired Y position in NED frame.
            z (float): Desired Z position in NED frame (negative for upward altitude).
            yaw (float): Desired yaw angle in radians.
        """
        msg = TrajectorySetpoint()
        msg.position = [x, y, z]
        msg.yaw = yaw
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.trajectory_setpoint_publisher.publish(msg)
        # Using debug level for frequent messages to avoid log spam during normal operation
        self.get_logger().debug(f"Publishing setpoints: Pos=[{x:.2f}, {y:.2f}, {z:.2f}], Yaw={yaw:.2f} rad")

    def publish_vehicle_command(self, command: int, **params) -> None:
        """
        Publishes a VehicleCommand message.
        Args:
            command (int): The PX4 vehicle command ID (e.g., VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM).
            **params: Optional parameters for the command (param1 to param7).
        """
        msg = VehicleCommand()
        msg.command = command
        # Populate optional parameters if provided
        msg.param1 = params.get("param1", 0.0)
        msg.param2 = params.get("param2", 0.0)
        msg.param3 = params.get("param3", 0.0)
        msg.param4 = params.get("param4", 0.0)
        msg.param5 = params.get("param5", 0.0)
        msg.param6 = params.get("param6", 0.0)
        msg.param7 = params.get("param7", 0.0)
        # Standard fields for vehicle commands
        msg.target_system = 1
        msg.target_component = 1
        msg.source_system = 1
        msg.source_component = 1
        msg.from_external = True
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vehicle_command_publisher.publish(msg)

    def timer_callback(self) -> None:
        """
        Callback function for the main control timer.
        This function is executed periodically and manages the vehicle's state transitions
        and setpoint publishing based on the current `self.current_state`.
        """
        # Always publish the offboard control heartbeat signal to keep offboard mode active
        self.publish_offboard_control_heartbeat_signal()

        if self.current_state == self.STATE_ARMING_OFFBOARD:
            # In this state, we send a few initial setpoints to prepare for offboard engagement.
            # This is a common practice to ensure PX4 is ready to accept offboard commands.
            if self.offboard_setpoint_counter < 10:
                # Send the initial takeoff height as the target during this phase
                self.publish_position_setpoint(0.0, 0.0, self.takeoff_height, self.target_yaw)
                self.offboard_setpoint_counter += 1
            else:
                # After sending initial setpoints, engage offboard mode and arm the vehicle
                self.engage_offboard_mode()
                self.arm()
                self.current_state = self.STATE_TAKEOFF  # Transition to takeoff state
                self.get_logger().info("Transitioned to TAKEOFF state.")
                # Ensure target for takeoff is correctly set
                self.target_x = 0.0
                self.target_y = 0.0
                self.target_z = self.takeoff_height

        elif self.current_state == self.STATE_TAKEOFF:
            # In this state, the vehicle is climbing to the desired takeoff height.
            # We continuously publish the takeoff setpoint.
            self.publish_position_setpoint(0.0, 0.0, self.takeoff_height, self.target_yaw)

            # Check if the vehicle has reached the takeoff height.
            # We use absolute difference and a small tolerance (0.2m) due to floating point comparisons
            # and potential oscillations around the target.
            # Note: vehicle_local_position.z is negative for altitude above home.
            if abs(self.vehicle_local_position.z - self.takeoff_height) < 0.2:
                self.get_logger().info(f"Reached takeoff height of {self.takeoff_height} m. Holding position.")
                self.current_state = self.STATE_HOLD_AND_LISTEN  # Transition to hold state
                # Set the target position to the current vehicle position to hold
                self.target_x = self.vehicle_local_position.x
                self.target_y = self.vehicle_local_position.y
                self.target_z = self.vehicle_local_position.z
                # Keep the last published yaw or set a specific hold yaw
                self.get_logger().info("Transitioned to HOLD_AND_LISTEN state, awaiting dynamic setpoints.")

        elif self.current_state == self.STATE_HOLD_AND_LISTEN:
            # In this state, the vehicle holds its current position and yaw,
            # waiting for the first dynamic setpoint command from another node.
            # It will transition to STATE_MISSION once a PoseStamped message is received.
            self.publish_position_setpoint(self.target_x, self.target_y, self.target_z, self.target_yaw)

        elif self.current_state == self.STATE_MISSION:
            # In this state, the vehicle actively follows the dynamically updated setpoints.
            # `self.target_x`, `self.target_y`, `self.target_z`, `self.target_yaw` are
            # updated by the `dynamic_setpoint_callback` whenever a new message arrives.
            self.publish_position_setpoint(self.target_x, self.target_y, self.target_z, self.target_yaw)

            # Simple heuristic to trigger landing:
            # If the commanded target_z is near the ground (e.g., above -0.5m)
            # AND the vehicle's actual position is also relatively low (e.g., within 1m of ground)
            # This prevents accidental landing if a high altitude target_z is commanded.
            # A more robust landing trigger would be a dedicated "land" command topic.
            if self.target_z > -0.5 and abs(self.vehicle_local_position.z) < 1.0:
                self.get_logger().info("Target Z indicates landing. Initiating landing sequence.")
                self.current_state = self.STATE_LANDING  # Transition to landing state

        elif self.current_state == self.STATE_LANDING:
            # In this state, the vehicle is commanded to land.
            # We continuously send the land command. PX4 will handle the landing maneuver.
            self.land()
            # Optional: Add logic to terminate the node after successful landing
            # (e.g., check for VehicleStatus.NAVIGATION_STATE_IDLE or disarmed state)
            # For this example, the node will keep running until manually stopped (Ctrl+C).


def main(args=None) -> None:
    """Main function to initialize and run the ROS 2 node."""
    print('Starting offboard control node with dynamic setpoints...')
    rclpy.init(args=args)  # Initialize ROS 2 client library
    offboard_control = OffboardControl()  # Create an instance of the node
    try:
        rclpy.spin(offboard_control)  # Keep the node running and process callbacks
    except KeyboardInterrupt:
        # Handle Ctrl+C for a graceful shutdown
        pass
    finally:
        # Ensure the node is properly destroyed and ROS 2 shutdown
        offboard_control.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        # Catch any exceptions during execution and print them
        print(f"An error occurred: {e}")

