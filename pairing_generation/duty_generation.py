# importing the packages
import numpy as np
import pandas as pd
from warnings import filterwarnings

filterwarnings("ignore")


def generate_duties_dfs(np_arr, current_duty, valid_duty):
    if is_valid_duty(np_arr, current_duty):
        valid_duty.append(current_duty.copy().tolist())
        return
    if len(current_duty) == 3:
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
        (time_difference <= np.timedelta64(3, "h"))
    )


# total time constraint and return to homebase constraint
def is_valid_duty(np_arr, current_duty):
    # Implement conditions for pair validity
    return (
        np_arr[current_duty[0]][1] == np_arr[current_duty[-1]][2]
    ) and (  # return to homebase condition
        (np_arr[current_duty[-1]][4] - np_arr[current_duty[0]][3])
        <= np.timedelta64(8, "h")
    )


def generate_duties():
    # reading the dataframe
    df = pd.read_csv("data/flight_legs/data.csv")
    df["start_time"] = pd.to_datetime(df["start_time"], format="%Y-%m-%d %H:%M:%S")
    df["end_time"] = pd.to_datetime(df["end_time"], format="%Y-%m-%d %H:%M:%S")

    # convert the dataframe to a numpy array
    np_arr = df.to_numpy()

    # Create an empty list to hold the duties
    valid_duty_dfs = []

    # Start DFS from each flight leg
    for start_leg in range(len(np_arr)):
        generate_duties_dfs(np_arr, np.array([start_leg]), valid_duty_dfs)

    # Open the file in write mode
    with open(f"data/duties/duties.txt", "w") as file:
        file.writelines(f"{item}\n" for item in valid_duty_dfs)
