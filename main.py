def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """

    # for removed_values in cleaned_list:
    # CREATE EMPTY LIST, WE'LL APPEND CLEANED HEARTRATE VALUES IN L8R
    cleaned_list = []
    removed_values = 0
    
    for heartrate in data:
        stripped_heartrate = heartrate.strip()
        if stripped_heartrate.isdigit() is True:
            stripped_heartrate = (int(stripped_heartrate))
            cleaned_list.append(stripped_heartrate)
        else: # if the value fails a digit check add 1 to removed_values
            removed_values = removed_values + 1
            
                           
    return (cleaned_list, removed_values)

    pass


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
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

    ordered_data = sorted(data)
    # print(ordered_data)
    length = len(ordered_data)
    middle_index = length // 2
    
    # mid1, mid2 are the two mddle numbers when a list is sorted... we take the average of them to get median when the list' length is even
    # else, 
    if length % 2 == 0:
        mid1 = ordered_data[middle_index]
        mid2 = ordered_data[middle_index - 1]
        middle_num = mid1 + mid2 
        even_median = round(middle_num / 2, 2)

        return even_median
    else:
        odd_median = ordered_data[middle_index]

        return odd_median
        
    
    return ordered_data[middle_index] 
    
    pass


def range(data: list) -> float:
    """
    """
    pass


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
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
    # print out your data quality measure to the console
    print(cleaned_list, removed_values)

    median_heart_rate_data = median(cleaned_list)
    print("Median", median_heart_rate_data)


    # print out your descriptive statistics to the console
    # ...we are passing in the strings that are in the path of the text filesif __name__ == "__main__":
if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
    
    # data(close) ??
# print("Is this thing even working LOL!")

