def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    users_online = 0

    for init_time, end_time in permanence_period:
        if not init_time or not end_time:
            return None
        if init_time <= target_time <= end_time:
            users_online += 1
    return users_online
