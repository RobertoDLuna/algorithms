def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    users_online = 0

    # para cada intervalo de entrada e saida em permanence_period
    for init_time, end_time in permanence_period:
        #se não tiver entrada ou saida, retorna none
        if not init_time or not end_time:
            return None
        if init_time <= target_time <= end_time:
            users_online += 1
    return users_online