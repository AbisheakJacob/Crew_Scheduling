# importing the packages
import numpy as np
import pandas as pd
from itertools import chain


# DFS function to generate all possible pairs
def generate_pairs_dfs(np_arr, duties, current_pair, valid_pairs, a):
    if len(current_pair) == a:
        valid_pairs.append(current_pair.copy())
        return

    for duty in [
        duties[i]
        for i in range(len(duties))
        if (np_arr[duties[i][0]][1] == np_arr[current_pair[-1][-1]][2])
        and (
            np_arr[duties[i][0]][3] - np_arr[current_pair[-1][-1]][4]
            >= np.timedelta64(10, "h")
            and (np_arr[duties[i][0]][3] - np_arr[current_pair[-1][-1]][4])
            <= np.timedelta64(15, "h")
        )
    ]:
        current_pair.append(duty)
        generate_pairs_dfs(np_arr, duties, current_pair, valid_pairs, a)
        current_pair.pop()  # Backtrack


# Function to check if the pair is valid
def is_valid_pair(np_arr, current_pair, pair_time):
    if len(current_pair) >= 2:
        return (
            np_arr[current_pair[-1][-1]][4] - np_arr[current_pair[0][0]][3]
        ) >= np.timedelta64(18, "h")
    else:
        return False


# Function to generate pairs
def generate_pairs():
    # Reading the dataframe and converting it to a numpy array
    np_arr = pd.read_csv(
        "data/flight_legs/data.csv",
        parse_dates=["start_time", "end_time"],
    ).to_numpy()

    # read the duties from the txt file
    with open("data/duties/duties.txt") as file:
        duties = [eval(line) for line in file]

    # create a list to hold the valid pairs
    valid_pair_dfs = []

    # call the function to generate pairs
    for a in range(2, 4):
        for duty in duties:
            generate_pairs_dfs(np_arr, duties, [duty], valid_pair_dfs, a)

    # save the pairings as a txt file
    with open(f"data/pairings/pairings.txt", "w") as file:
        file.writelines(f"{item}\n" for item in valid_pair_dfs)


# Driver code
generate_pairs()
