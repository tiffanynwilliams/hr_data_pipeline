
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
