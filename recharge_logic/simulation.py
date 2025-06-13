
from drone import Drone
from controller import manage_drones
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon

# Define field boundary (convex polygon)
field_boundary = [(0, 0), (300, 50), (250, 150), (50, 200), (-50, 100)]

# Initialize drones with field boundary
drone_a = Drone(drone_id='A', role='coverage', speed=5, drain_rate=0.002, 
               position=(0, 0), field_boundary=field_boundary)
drone_b = Drone(drone_id='B', role='irrigation', speed=4, drain_rate=0.003, 
               position=(0, 0), tank_capacity=100, field_boundary=field_boundary)

# Set up the figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Systematic Field Coverage with Drones', fontsize=16)

# Subplot 1: Movement paths
ax1.set_xlim(min(x for x,y in field_boundary)-20, max(x for x,y in field_boundary)+20)
ax1.set_ylim(min(y for x,y in field_boundary)-20, max(y for x,y in field_boundary)+20)
ax1.set_xlabel("X Position (m)")
ax1.set_ylabel("Y Position (m)")
ax1.set_title("Drone Movement Paths")
ax1.grid(True)

# Draw field boundary
field_poly = Polygon(field_boundary, closed=True, fill=False, color='black', linestyle='--')
ax1.add_patch(field_poly)

# Base station marker
ax1.plot(0, 0, 'ro', markersize=10, label='Base Station')

# Initialize drone path lines
line_a, = ax1.plot([], [], 'b-', alpha=0.3, label='Drone A (Coverage)')
line_b, = ax1.plot([], [], 'g-', alpha=0.3, label='Drone B (Irrigation)')
point_a = ax1.plot([], [], 'bo', markersize=8)[0]
point_b = ax1.plot([], [], 'gs', markersize=8)[0]
status_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes)
ax1.legend()

# Subplot 2: Battery levels over time
ax2.set_xlim(0, 500)
ax2.set_ylim(0, 1.1)
ax2.set_xlabel("Time (steps)")
ax2.set_ylabel("Battery Level")
ax2.set_title("Battery Levels Over Time")
ax2.grid(True)

# Initialize battery level lines
battery_line_a, = ax2.plot([], [], 'b-', label='Drone A Battery')
battery_line_b, = ax2.plot([], [], 'g-', label='Drone B Battery')
ax2.legend()

# Store data for plotting
time_points = []
battery_a = []
battery_b = []

def init():
    line_a.set_data([], [])
    line_b.set_data([], [])
    point_a.set_data([], [])
    point_b.set_data([], [])
    battery_line_a.set_data([], [])
    battery_line_b.set_data([], [])
    status_text.set_text('')
    return line_a, line_b, point_a, point_b, battery_line_a, battery_line_b, status_text

def update(frame):
    # Run simulation for one time step
    manage_drones(drone_a, drone_b, frame)
    drone_a.update(frame)
    drone_b.update(frame)
    
    # Update movement plot
    line_a.set_data(drone_a.x_history, drone_a.y_history)
    line_b.set_data(drone_b.x_history, drone_b.y_history)
    point_a.set_data([drone_a.position[0]], [drone_a.position[1]])
    point_b.set_data([drone_b.position[0]], [drone_b.position[1]])
    
    # Update status text
    status_text.set_text(
        f'Drone A: {drone_a.status}\nBattery: {drone_a.battery:.1%}\n'
        f'Drone B: {drone_b.status}\nBattery: {drone_b.battery:.1%}\n'
        f'Tank: {drone_b.tank_level}/{drone_b.tank_capacity}'
    )
    
    # Update battery plot
    time_points.append(frame)
    battery_a.append(drone_a.battery)
    battery_b.append(drone_b.battery)
    battery_line_a.set_data(time_points, battery_a)
    battery_line_b.set_data(time_points, battery_b)
    
    # Adjust view if needed
    if frame > 100:
        ax2.set_xlim(0, frame + 10)
    
    return line_a, line_b, point_a, point_b, battery_line_a, battery_line_b, status_text

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 2000, 1),
                    init_func=init, blit=False, interval=50)

plt.tight_layout()
plt.show()
