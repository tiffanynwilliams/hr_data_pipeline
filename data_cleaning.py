
def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    # cleaned_list will contain the stripped_heartrate values
    # removed_values is a counter for how many non-digit characters in the data

    cleaned_list = []
    removed_val = 0 
    
    # stripped_heartrate will have its integer-type heart rate values placed inside the cleaned_list
    # return cleaned_list and removed_values back to run()
    for heartrate in data:
        stripped_heartrate = heartrate.strip()
        if stripped_heartrate.isdigit() is True:
            stripped_heartrate = (int(stripped_heartrate))
            cleaned_list.append(stripped_heartrate)
        else: 
            # 
            removed_val = removed_val + 1     
                           
    return (cleaned_list, removed_val)

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