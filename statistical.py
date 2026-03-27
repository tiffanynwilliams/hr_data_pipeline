import math

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    # avg_heart_rate is the two decimal-place rounded total / length of data list
    # return the avg_heart_rate back to run()
    total = 0
    for heartrate in data:
        total += heartrate
        avg_heart_rate = round(total / len(data), 2)

    pass

    return avg_heart_rate

def median(data: list) -> float:
    """
    To find the median, follow these steps: 
    Sort the list with sorted() to save the ordered list to a new variable, find the middle using len(), and handle odd and even cases with if/else
    """
    # ordered_data is the data list with its heart rate values in ascending order
    # middle_index uses the length of ordered_data list and floor division to get an integer index
    ordered_data = sorted(data)
    length = len(ordered_data)
    middle_index = length // 2
    
    # mid1, mid2 are the two mddle numbers when a list is sorted... we take the average of them to get median when the list' length is even
    # return the middle number when the list is sorted... there is only one number when a length of a list is odd
    # return 2 decimal rounded ordered_even_median and odd_median back to run()
    if length % 2 == 0:
        mid1 = ordered_data[middle_index]
        mid2 = ordered_data[middle_index - 1]
        mid_num = mid1 + mid2 
        even_median = round(mid_num / 2, 2)

        return even_median
        
    else:

        odd_median = round(ordered_data[middle_index], 2)
        return odd_median
    
    pass

def range(data: list) -> float:
    """
    Range is the cleaned_list's maximum - minimum.
    """
    # make an initial max_value to first heartrate value in data list
    max_val = data[0]

    # max_val is updated to heartrate if heartrate is larger than max_val
    for heartrate in data:
        if heartrate > max_val:
            max_val = heartrate
    
    # make an initial min_value to first heartrate value in data list
    min_val = data[0]
    # min_val is updated to heartrate if heartrate is smaller than min_val
    for heartrate in data:
        if heartrate < min_val:
            min_val = heartrate
        
    heartrate_range = max_val - min_val
      
    return heartrate_range


    pass

def variance(data: list) -> float:
    """
    Variance is the average of the squared differences from the mean. 
    We have the mean from average(); use a for loop to iterate over data, 
    round the variance to nearest hundreth for standard deviation.
    
    """
    mean = average(data)
    
    squared_sums = 0

    for heartrate in data:
        heartrate -= mean
        squared_vals = heartrate ** 2
        squared_sums += squared_vals
    
    variance_result = round(squared_sums / (len(data)), 2)

    standard_dev = round(math.sqrt(variance_result), 2)

    return (variance_result, standard_dev)
