import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
<<<<<<< HEAD
from drone_interfaces.msg import DroneStatus, WaypointRequest
=======
from drone_interfaces.msg import DroneStatus, WaypointRequest, GeotagRequest
>>>>>>> dual_drone


class SwarmSupervisorNode(Node):

    def __init__(self):
        super().__init__('swarm_supervisor_node')
        self.get_logger().info("Swarm Supervisor Node Started.")

        self.drone_status = {}
        self.last_seen = {}
<<<<<<< HEAD
        # Keep track of actively dispatched drones for the *current* task
        self.actively_dispatched = set() 

=======
        self.actively_dispatched = set()
>>>>>>> dual_drone
        self.timeout_sec = 10.0

        # Subscriptions
        self.create_subscription(DroneStatus, '/drone_1/status', self.status_callback, 10)
        self.create_subscription(DroneStatus, '/drone_2/status', self.status_callback, 10)

        # Publishers
        self.waypoint_pub = self.create_publisher(WaypointRequest, '/waypoint_manager/request', 10)
<<<<<<< HEAD
        self.geotag_pub = self.create_publisher(WaypointRequest, '/geotag_manager/request', 10)
=======
        self.geotag_pub = self.create_publisher(GeotagRequest, '/geotag_manager/request', 10)
>>>>>>> dual_drone

        # Timer
        self.create_timer(2.0, self.check_for_unpaired_drones)

    def status_callback(self, msg: DroneStatus):
        now = self.get_clock().now()

        drone_id = msg.drone_id
        drone_type = msg.type.lower().strip()
        drone_status = msg.status.lower().strip()
        direction = msg.direction.strip().lower() or 'top'

        self.get_logger().info(f"[{drone_id}] status: {drone_status}, type: {drone_type}, direction: {direction}")

<<<<<<< HEAD
        # Update status and last seen time for all drones
        self.drone_status[drone_id] = msg
        self.last_seen[drone_id] = now

        # If a drone reports 'idle' and was previously dispatched, remove it from actively_dispatched
=======
        self.drone_status[drone_id] = msg
        self.last_seen[drone_id] = now

>>>>>>> dual_drone
        if drone_status == 'idle' and drone_id in self.actively_dispatched:
            self.get_logger().info(f"[{drone_id}] is now idle. Removing from actively_dispatched set.")
            self.actively_dispatched.remove(drone_id)

<<<<<<< HEAD
        # Only process for dispatching if the drone is 'idle' AND not currently marked as actively dispatched
        # and has a valid type for dispatching
        if drone_status != 'idle' or drone_type not in ['surveillance', 'irrigation'] or drone_id in self.actively_dispatched:
            return

        # Check if other drone is known
=======
        if drone_status != 'idle' or drone_type not in ['surveillance', 'irrigation'] or drone_id in self.actively_dispatched:
            return

>>>>>>> dual_drone
        other_id = 'drone_2' if drone_id == 'drone_1' else 'drone_1'

        if other_id in self.drone_status and other_id not in self.actively_dispatched:
            other = self.drone_status[other_id]
            other_type = other.type.lower().strip()
            other_direction = other.direction.strip().lower() or 'bottom'
            other_status = other.status.lower().strip()

<<<<<<< HEAD
            # Only attempt to pair if the other drone is also idle and not actively dispatched
=======
>>>>>>> dual_drone
            if other_status == 'idle' and other_type in ['surveillance', 'irrigation']:
                if other_type == drone_type:
                    new_direction = 'bottom' if other_direction == 'top' else 'top'
                    self.send_request(drone_type, drone_id, new_direction)
<<<<<<< HEAD
                    self.send_request(other_type, other.drone_id, other_direction) # Send request for both
                else:
                    self.send_request(drone_type, drone_id, direction)
                    self.send_request(other_type, other.drone_id, other_direction)
                
                # Mark both drones as actively dispatched if they formed a pair
=======
                    self.send_request(other_type, other.drone_id, other_direction)
                else:
                    self.send_request(drone_type, drone_id, direction)
                    self.send_request(other_type, other.drone_id, other_direction)

>>>>>>> dual_drone
                self.actively_dispatched.add(drone_id)
                self.actively_dispatched.add(other.drone_id)
            else:
                self.get_logger().info(f"{other_id} is not idle or already dispatched. Waiting for timeout...")
        else:
            self.get_logger().info(f"{other_id} not yet active or already dispatched. Waiting for timeout...")

<<<<<<< HEAD

    def check_for_unpaired_drones(self):
        now = self.get_clock().now()
        self.get_logger().info("Checking for unpaired drones...")
        
        for drone_id in list(self.drone_status.keys()): # Iterate over a copy to allow modification during loop
            # If a drone is currently actively dispatched, skip it for solo dispatching
=======
    def check_for_unpaired_drones(self):
        now = self.get_clock().now()
        self.get_logger().info("Checking for unpaired drones...")

        for drone_id in list(self.drone_status.keys()):
>>>>>>> dual_drone
            if drone_id in self.actively_dispatched:
                continue

            msg = self.drone_status[drone_id]
            last_seen = self.last_seen.get(drone_id)
<<<<<<< HEAD
            
            # Only consider idle drones for solo dispatch
=======

>>>>>>> dual_drone
            if msg.status.lower().strip() != 'idle':
                continue

            if not last_seen:
                continue

<<<<<<< HEAD
            # Check if the OTHER drone has timed out or is not active
            other_id = 'drone_2' if drone_id == 'drone_1' else 'drone_1'
            other_last_seen = self.last_seen.get(other_id)
            
            # Check if other drone is known and active (not timed out)
            other_is_active = other_id in self.drone_status and \
                              (other_last_seen and (now - other_last_seen) <= Duration(seconds=self.timeout_sec))

            # If the current drone is idle and the other drone is *not* active (timed out or unknown)
            # OR if the other drone *is* active but is already dispatched (unlikely to form a pair now)
            # then dispatch the current drone solo.
=======
            other_id = 'drone_2' if drone_id == 'drone_1' else 'drone_1'
            other_last_seen = self.last_seen.get(other_id)

            other_is_active = other_id in self.drone_status and \
                              (other_last_seen and (now - other_last_seen) <= Duration(seconds=self.timeout_sec))

>>>>>>> dual_drone
            if not other_is_active or (other_id in self.actively_dispatched):
                direction = msg.direction.strip().lower() or 'top'
                self.get_logger().warn(f"{other_id} is offline, timed out (> {self.timeout_sec}s), or actively dispatched. Dispatching {drone_id} solo.")
                self.send_request(msg.type.lower().strip(), drone_id, direction)
<<<<<<< HEAD
                self.actively_dispatched.add(drone_id) # Mark as actively dispatched

            else:
                # If the other drone is still active, idle, and not dispatched, continue waiting for pair.
                self.get_logger().info(f"{drone_id} is active and idle, and {other_id} is also active and idle. Waiting for pair.")


    def send_request(self, drone_type: str, drone_id: str, direction: str):
        req = WaypointRequest()
        req.drone_id = drone_id
        req.direction = direction

        if drone_type == 'surveillance':
            self.get_logger().info(f"[{drone_id}] → Sending to /waypoint_manager/request from {direction}")
            self.waypoint_pub.publish(req)
        elif drone_type == 'irrigation':
=======
                self.actively_dispatched.add(drone_id)
            else:
                self.get_logger().info(f"{drone_id} is active and idle, and {other_id} is also active and idle. Waiting for pair.")

    def send_request(self, drone_type: str, drone_id: str, direction: str):
        if drone_type == 'surveillance':
            req = WaypointRequest()
            req.drone_id = drone_id
            req.direction = direction
            self.get_logger().info(f"[{drone_id}] → Sending to /waypoint_manager/request from {direction}")
            self.waypoint_pub.publish(req)
        elif drone_type == 'irrigation':
            req = GeotagRequest()
            req.drone_id = drone_id
            req.direction = direction
>>>>>>> dual_drone
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
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> dual_drone
