import matplotlib.pyplot as plt 

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