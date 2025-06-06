
import math
from recharge import should_return_to_base

class Drone:
    def __init__(self, drone_id, role, speed, drain_rate, position, tank_capacity=None, field_boundary=None):
        self.id = drone_id
        self.role = role
        self.speed = speed
        self.drain_rate = drain_rate
        self.position = position
        self.base_position = (0, 0)
        self.battery = 2.0
        self.tank_capacity = tank_capacity
        self.tank_level = tank_capacity if tank_capacity else None
        self.recharge_history = []
        self.status = 'active'
        self.time = 0
        self.x_history = []
        self.y_history = []
        self.field_boundary = field_boundary or [(0, 0), (200, 0), (200, 100), (0, 100)]
        self.swath_width = 10
        self.direction = 1
        self.coverage_path = self.generate_coverage_path()
        self.current_path_index = 0
        self.last_working_position = None
        self.charging_start_time = None
        self.charging_duration = 50  # Charging time in time units

    def generate_coverage_path(self):
        """Generate coverage path for the field"""
        if not self.field_boundary:
            return []
            
        min_x = min(p[0] for p in self.field_boundary)
        max_x = max(p[0] for p in self.field_boundary)
        min_y = min(p[1] for p in self.field_boundary)
        max_y = max(p[1] for p in self.field_boundary)
        
        path = []
        y = min_y + self.swath_width/2
        
        while y <= max_y:
            if self.direction == 1:
                path.append((min_x, y))
                path.append((max_x, y))
            else:
                path.append((max_x, y))
                path.append((min_x, y))
            y += self.swath_width
            self.direction *= -1
            
        return path

    def distance_from_base(self):
        dx = self.position[0] - self.base_position[0]
        dy = self.position[1] - self.base_position[1]
        return math.hypot(dx, dy)

    def update(self, current_time):
        self.time = current_time
        self.x_history.append(self.position[0])
        self.y_history.append(self.position[1])

        if self.status == 'active':
            if should_return_to_base(self.battery, self.drain_rate, self.distance_from_base()):
                self.last_working_position = self.position
                self.status = 'returning'
            else:
                self.follow_coverage_path()
                self.consume_battery()
                if self.role == 'irrigation':
                    self.tank_level -= 1
                    if self.tank_level <= 0:
                        self.last_working_position = self.position
                        self.status = 'returning'
        elif self.status == 'returning':
            self.move_towards_base()
            self.consume_battery()
            if self.position == self.base_position:
                self.status = 'waiting_to_charge'
                # Instantly refill tank if drone has a tank
                if self.tank_capacity is not None:
                    self.tank_level = self.tank_capacity

        elif self.status == 'waiting_to_charge':
            pass  # Controller manages charging queue

        elif self.status == 'charging':
            if current_time - self.charging_start_time >= self.charging_duration:
                self.battery = 2.0
                if hasattr(self, 'shared_charging_queue') and self.id in self.shared_charging_queue:
                    self.shared_charging_queue.remove(self.id)
                    self.recharge_history.append(current_time)
                
                if self.last_working_position:
                    self.status = 'returning_to_work'
                    self.return_target = self.last_working_position
                    self.last_working_position = None
                else:
                    self.status = 'active'
                    self.coverage_path = self.generate_coverage_path()
                    self.current_path_index = 0

        elif self.status == 'returning_to_work':
            x, y = self.position
            tx, ty = self.return_target
            dx = tx - x
            dy = ty - y
            dist = math.hypot(dx, dy)
            
            if dist < self.speed:
                self.position = self.return_target
                self.status = 'active'
            else:
                self.position = (
                    x + self.speed * dx / dist,
                    y + self.speed * dy / dist
                )
            self.consume_battery()

    def follow_coverage_path(self):
        if not self.coverage_path or self.current_path_index >= len(self.coverage_path):
            return
            
        target = self.coverage_path[self.current_path_index]
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        distance = math.hypot(dx, dy)
        
        if distance < self.speed:
            self.position = target
            self.current_path_index = (self.current_path_index + 1) % len(self.coverage_path)
        else:
            self.position = (
                self.position[0] + self.speed * dx / distance,
                self.position[1] + self.speed * dy / distance
            )

    def move_towards_base(self):
        x, y = self.position
        bx, by = self.base_position
        dx = bx - x
        dy = by - y
        dist = math.hypot(dx, dy)
        if dist < self.speed:
            self.position = self.base_position
        else:
            self.position = (x + self.speed * dx / dist, y + self.speed * dy / dist)

    def consume_battery(self):
        self.battery -= self.drain_rate * self.speed
