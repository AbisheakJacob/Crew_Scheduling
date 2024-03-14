# importing the packages
import numpy as np
import pandas as pd
from itertools import chain
from warnings import filterwarnings

filterwarnings("ignore")


#  DFS function to generate all possible duties
def generate_duties_dfs(np_arr, current_duty, valid_duty):
    if is_valid_duty(np_arr, current_duty):
        valid_duty.append(current_duty.copy().tolist())
        return
    if len(current_duty) == 3:  # this is a depth limiter
        return

    # Recursive DFS for each remaining flight leg
    for index in np.where(np_arr[:, 1] == np_arr[current_duty[-1]][2])[0]:
        # Check if the leg can be added to the current pair
        if sub_df(np_arr, current_duty, index):
            current_duty = np.append(current_duty, index)
            generate_duties_dfs(np_arr, current_duty, valid_duty)
            current_duty = current_duty[:-1]  # Backtrack


# function taking care of the time constraint and total time constraint
def sub_df(np_arr, current_duty, index):
    time_difference = np_arr[index][3] - np_arr[current_duty[-1]][4]
    return ((time_difference >= np.timedelta64(1, "h"))) and (
        (time_difference <= np.timedelta64(5, "h"))
    )


# total time constraint and return to homebase constraint
def is_valid_duty(np_arr, current_duty):
    return (np_arr[current_duty[0]][1] == np_arr[current_duty[-1]][2]) and (
        (np_arr[current_duty[-1]][4] - np_arr[current_duty[0]][3])
        <= np.timedelta64(9, "h")
    )


# function to generate all possible duties
def generate_duties():
    # Reading the dataframe and converting it to a numpy array
    np_arr = pd.read_csv(
        "data/flight_legs/data.csv",
        parse_dates=["start_time", "end_time"],
        infer_datetime_format=True,
    ).to_numpy()
    # Create an empty list to hold the duties
    valid_duty_dfs = []

    # Start DFS from each flight leg
    for start_leg in range(len(np_arr)):
        generate_duties_dfs(np_arr, np.array([start_leg]), valid_duty_dfs)

    # Open the file in write mode
    with open(f"data/duties/duties.txt", "w") as file:
        file.writelines(f"{item}\n" for item in valid_duty_dfs)


# define the function to check if all the flight legs are covered
def duty_check():
    # Open the file in read mode
    with open("data/duties/duties.txt", "r") as file:
        lines = file.readlines()

    # convert each line (representing a list) to an actual list
    duties = [eval(line) for line in lines]

    duty = list(set(chain(*duties)))

    return len(duties), len(duty)
