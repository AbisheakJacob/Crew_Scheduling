# importing the packages
import numpy as np
import pandas as pd


# function to get the data information
def data_info():
    np_arr = pd.read_csv(
        "data/flight_legs/data.csv",
        parse_dates=["start_time", "end_time"],
        infer_datetime_format=True,
    ).to_numpy()

    # find the lowest time in column 2 and the highest time in column 3 to get the total time in days
    lowest_time = min(np_arr[:, 3])
    highest_time = max(np_arr[:, 4])
    total_time = highest_time - lowest_time

    # find the total time in days
    total_time = total_time / np.timedelta64(1, "D")
    num_days = round(total_time)

    # find the length of column number 0
    num_flights = len(np_arr[:, 0])

    # find all the unique values in column 1
    airports = np.unique(np_arr[:, 1])

    # find the count of the airports
    num_airports = len(airports)

    # find the count of the
    return num_days, num_flights, num_airports
