def should_return_to_base(battery_level, battery_drain_rate, distance_from_base, safety_margin=0.05):
    """
    Determine if the drone should return to the base station for recharge.
    """
    required_battery_to_return = distance_from_base * battery_drain_rate
    return battery_level <= (required_battery_to_return + safety_margin)


def predict_next_recharge(recharge_history):
    """
    Predict the next recharge timestamp based on the average of last 3 recharge intervals.
    """
    if len(recharge_history) < 3:
        return None  # Not enough data to predict
    intervals = [recharge_history[i+1] - recharge_history[i] for i in range(2)]
    avg_interval = sum(intervals) / len(intervals)
    return recharge_history[-1] + avg_interval