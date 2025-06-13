from drone import Drone

def manage_drones(drone_a, drone_b, current_time):
    if not hasattr(drone_a, 'shared_charging_queue'):
        drone_a.shared_charging_queue = []

    charging_queue = drone_a.shared_charging_queue
    drone_b.shared_charging_queue = charging_queue

    # Add to queue if drone is waiting to charge and not already in queue
    if drone_a.status == 'waiting_to_charge' and drone_a.id not in charging_queue:
        charging_queue.append(drone_a.id)

    if drone_b.status == 'waiting_to_charge' and drone_b.id not in charging_queue:
        charging_queue.append(drone_b.id)

    # Manage current charger
    if charging_queue:
        current_charger = charging_queue[0]

        if current_charger == drone_a.id and drone_a.status == 'waiting_to_charge':
            drone_a.status = 'charging'
            drone_a.charging_start_time = current_time

        elif current_charger == drone_b.id and drone_b.status == 'waiting_to_charge':
            drone_b.status = 'charging'
            drone_b.charging_start_time = current_time

