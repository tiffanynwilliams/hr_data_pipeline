def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    
    # remove the instances of ' ' and 'NO DATA' first and in this f(x)
    # return cleaned_list, removed_values = clean_heartrate_data(data) 

    # for removed_values in cleaned_list:
    #     print(float(cleaned_list.strip()))

    # CREATE EMPTY LIST, WE'LL APPEND CLEANED HEARTRATE VALUES IN L8R
    cleaned_list = []
    removed_values = 0
    
    for heartrate in data:
            stripped_heartrate = heartrate.strip()
    if stripped_heartrate.isdigit() is True:
            stripped_heartrate =(int(stripped_heartrate))
            cleaned_list.append(stripped_heartrate)
    else: # if the value fails a digit check add 1 to removed_values
            removed_values = removed_values + 1
           
            # print(cleaned_list, removed_values = clean_heartrate_data(data))

    return  cleaned_list, removed_values
   
        # print(heartrate.append(float(heartrate.strip)))

    pass


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    pass


def median(data: list) -> float:
    """
    """
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

    # testing! 

    # open file using file I/O and read it into the `data` list
    
    file_object = open(file)
    data = file_object.readlines()

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    # cleaned_list, removed_values = clean_heartrate_data(data) 

    # calculate the average, median, and range of this file using the functions you've wrote
    average_heart_rate_data = average(data)

    # print out your data quality measure to the console
    # ...

    # print out your descriptive statistics to the console
    # ...we are passing in the strings that are in the path of the text filesif __name__ == "__main__":
if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")

print("Is this thing even working LOL!")
