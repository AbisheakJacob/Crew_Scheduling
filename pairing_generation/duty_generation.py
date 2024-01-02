# generate duties

# importing the packages
import numpy as np
from numba import jit, cuda
import pandas as pd
from datetime import timedelta

#@jit(nopython=True)
def generate_duties_dfs(np_arr, current_duty, valid_duty):
    # Recursive DFS for each remaining flight leg
    if is_valid_duty(np_arr, current_duty):
        valid_duty.append(current_duty.copy())
        return
    if len(current_duty) == 3:
        return

    # Recursive DFS for each remaining flight leg
    #[slist for slist in range(len(np_arr)) if (np_arr[slist][1] == np_arr[current_duty[-1]][2])]
    #np.arange(len(np_arr))[np_arr[:,1] == np_arr[current_duty[-1]][2]]
    for index in np.where(np_arr[:,1] == np_arr[current_duty[-1]][2])[0]:
        # Check if the leg can be added to the current pair
        if sub_df(np_arr, current_duty, index):
            current_duty.append(index)
            generate_duties_dfs(np_arr, current_duty, valid_duty)
            current_duty.pop()  # Backtrack

# function taking care of the time constraint and total time constraint
#@jit(nopython=True)
def sub_df(np_arr, current_duty, index):
    return (
        ((np_arr[index][3] - np_arr[current_duty[-1]][4] >= timedelta(hours=1)))
        and
        ((np_arr[index][3] - np_arr[current_duty[-1]][4] <= timedelta(hours=3)))
    )

# total time constraint and return to homebase constraint
#@jit(nopython=True)
def is_valid_duty(np_arr, current_duty):
    # Implement conditions for pair validity
    # Ensure matching destination and departure airports, and time gaps
    return (
        (np_arr[current_duty[0]][1] == np_arr[current_duty[-1]][2])  # return to homebase condition
        and 
        ((np_arr[current_duty[-1]][4] - np_arr[current_duty[0]][3]) <= timedelta(hours=12))
    )

@jit(nopython=True)
def generate_duties():
    # reading the dataframe
    df = pd.read_csv("data/flight_legs/data.csv")
    df['start_time'] = pd.to_datetime(df['start_time'], format="%Y-%m-%d %H:%M:%S")
    df['end_time'] = pd.to_datetime(df['end_time'], format="%Y-%m-%d %H:%M:%S")

    # convert the dataframe to a numpy array
    np_arr = df.to_numpy()

    # Create an empty list to hold the duties
    valid_duty_dfs = []

    # Start DFS from each flight leg
    for start_leg in range(len(np_arr)):
        generate_duties_dfs(np_arr, [start_leg], valid_duty_dfs)

    # Open the file in write mode
    with open(f"data/duties/duties.txt", "w") as file:
        # Write each item in the list to a new line
        for item in valid_duty_dfs:
            file.write(f"{item}\n")