def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    # cleaned_list will contain the stripped_heartrate values
    # removed_values is a counter for how many non-digit characters in the data

    cleaned_list = []
    removed_values = 0
    
    # stripped_heartrate will have its integer-type heart rate values placed inside the cleaned_list
    # return cleaned_list and removed_values back to run()
    for heartrate in data:
        stripped_heartrate = heartrate.strip()
        if stripped_heartrate.isdigit() is True:
            stripped_heartrate = (int(stripped_heartrate))
            cleaned_list.append(stripped_heartrate)
        else: 
            removed_values = removed_values + 1     
                           
    return (cleaned_list, removed_values)

    pass


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
    range is the cleaned_list's maximum - minimum...   
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


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)  revist this after submitting TLAB
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    
    file_object = open(file)
    data = file_object.readlines()
    
    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)  
    
    # calculate the average, median, and range of this file using the functions you've wrote
    average_heart_rate_data = average(cleaned_list)
    print("Average:", average_heart_rate_data)   
    
    median_heart_rate_data = median(cleaned_list)
    print("Median:", median_heart_rate_data)

    range_heart_rate_data = range(cleaned_list)
    print("Range:", range_heart_rate_data)
    


    # print out your data quality measure to the console
    print(cleaned_list)

    
    #close() to stop reading the files
    file_object.close()

    # print out your descriptive statistics to the console
    # we are passing in the strings that are in the path of the text files
if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
    
    

