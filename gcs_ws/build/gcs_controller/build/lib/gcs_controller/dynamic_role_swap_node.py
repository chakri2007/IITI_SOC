#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from drone_interfaces.msg import DroneStatus, DroneTypeChange, SurveillanceStatus, DroneStatusUpdate

class DynamicRoleSwapNode(Node):
    def __init__(self):
        super().__init__('dynamic_role_swap_node')

        self.drone_ids = ['drone_1', 'drone_2']
        self.drone_statuses = {}
        self.surveillance_completed = False

        # Publishers for type change
        self.role_change_publishers = {
            drone_id: self.create_publisher(
                DroneTypeChange,
                f'/{drone_id}/type_change',
                10
            )
            for drone_id in self.drone_ids
        }

        # Publishers for status update
        self.status_update_publishers = {
            drone_id: self.create_publisher(
                DroneStatusUpdate,
                f'/{drone_id}/update_status',
                10
            )
            for drone_id in self.drone_ids
        }

        # Subscriptions
        for drone_id in self.drone_ids:
            self.create_subscription(
                DroneStatus,
                f'/{drone_id}/status',
                self.make_drone_status_callback(drone_id),
                10
            )
            self.create_subscription(
                Float32,
                f'/{drone_id}/water_level',
                self.make_water_level_callback(drone_id),
                10
            )

        self.create_subscription(
            SurveillanceStatus,
            '/surveillance_status',
            self.surveillance_status_callback,
            10
        )

        self.get_logger().info("Dynamic Role Swap Node initialized.")

    def make_drone_status_callback(self, drone_id):
        def callback(msg):
            self.drone_statuses[drone_id] = msg
            self.get_logger().debug(f"Updated status for {drone_id}: {msg}")
        return callback

    def make_water_level_callback(self, drone_id):
        def callback(msg):
            water_level = msg.data
            self.get_logger().debug(f"{drone_id} water level: {water_level:.2f}")

            if water_level < 0.01:
                if not self.surveillance_completed:
                    status = self.drone_statuses.get(drone_id)
                    if status and status.type.lower() == "irrigation":
                        self.get_logger().info(
                            f"{drone_id} has empty tank and surveillance incomplete → switching to surveillance"
                        )
                        self.swap_drone_role(drone_id, "surveillance")
        return callback

    def surveillance_status_callback(self, msg):
        self.get_logger().info(
            f"Surveillance status: completed={msg.surveillance_completed}, remaining={msg.waypoints_remaining}"
        )
        self.surveillance_completed = msg.surveillance_completed

        if msg.surveillance_completed:
            for drone_id in self.drone_ids:
                status = self.drone_statuses.get(drone_id)
                if status:
                    if status.type.lower() == "surveillance":
                        self.get_logger().info(
                            f"{drone_id} completed surveillance → switching to irrigation"
                        )
                        self.swap_drone_role(drone_id, "irrigation")
                else:
                    self.get_logger().warn(f"No status yet for {drone_id}, cannot evaluate type.")

    def swap_drone_role(self, drone_id, new_type):
        self.publish_type_change(drone_id, new_type)
        self.publish_status_update(drone_id, "idle")

    def publish_type_change(self, drone_id, new_type):
        msg = DroneTypeChange()
        msg.new_drone_type = new_type
        self.role_change_publishers[drone_id].publish(msg)
        self.get_logger().info(f"Sent role change to {drone_id}: {new_type}")

    def publish_status_update(self, drone_id, status):
        msg = DroneStatusUpdate()
        msg.drone_id = drone_id
        msg.status = status
        self.status_update_publishers[drone_id].publish(msg)
        self.get_logger().info(f"Sent status update to {drone_id}: {status}")

def main(args=None):
    rclpy.init(args=args)
    node = DynamicRoleSwapNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
