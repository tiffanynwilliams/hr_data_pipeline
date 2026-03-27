from data_cleaning import clean_heartrate_data
from statistical import average, median, range
import math
import matplotlib.pyplot as plt 

def variance(data: list) -> float:
    mean = average(data)
    
    squared_sums = 0

    for heartrate in data:
        heartrate -= mean
        squared_vals = heartrate ** 2
        squared_sums += squared_vals
    
    variance_result = round(squared_sums / (len(data)),2)

    standard_dev = round(math.sqrt(variance_result), 2)

    return (variance_result, standard_dev)

def line_plot(data: list):
    """
    Create a visualisation using the cleaned_heartrate_data's values,
    labelling the graph adaquetly.

    Args:
        cleaned_heartrate_data, the cleaned data list.
    
    Returns:
        None, should save an image to images/ folder
    """
    fig, ax = plt.subplots()

    ax.plot(data, color ='hotpink')
    ax.set_title("Heart Rate Data, Individual in 30s")
    ax.set_xlabel("Minutes")
    ax.set_ylabel("Heart Rate (bpm)")
    # save the image to the correct folder
    fig.savefig("images/heart_rate_graph.png")
    # best practice, helps with memory
    plt.close()


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
    cleaned_list, removed_val = clean_heartrate_data(data)  

    # calculate the average, median, and range of this file using the functions you've wrote
    average_heart_rate_data = average(cleaned_list)
    print("Average:", average_heart_rate_data, "bpm")   
    
    median_heart_rate_data = median(cleaned_list)
    print("Median:", median_heart_rate_data, "bpm")

    range_heart_rate_data = range(cleaned_list)
    print("Range:", range_heart_rate_data, "bpm")


    # unpack the returned variance_result and standard_dev 
  
    variance_heart_rate_data, standard_dev = variance(cleaned_list)
    print("Variance:", variance_heart_rate_data)

    print ("Standard Deviation:", standard_dev)
 
    # print a counter of removed values
    print("Removed Values:", removed_val, "heartrate(s)")
 
    # print out your data quality measure to the console
    print("Cleaned Heartrate Values:", cleaned_list, "\n")

    # call the line_plot() to save an image of the heart rate graph in images/ folder
    line_plot(cleaned_list)
    
    
    #close() to stop reading the files
    file_object.close()

    # print out your descriptive statistics to the console
    # we are passing in the strings that are in the path of the text files
if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")