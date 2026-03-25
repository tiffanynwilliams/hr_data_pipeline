import statistics as stats

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    # avg_heart_rate is the two decimal-place rounded total / length of data list
    # return the avg_heart_rate back to run()
    total = 0
    for heartrate in data:
        total = total + heartrate
        avg_heart_rate = round(total / len(data), 2)

    pass

    return avg_heart_rate