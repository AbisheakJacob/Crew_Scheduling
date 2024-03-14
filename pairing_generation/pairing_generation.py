# importing the packages
import numpy as np
import pandas as pd
from itertools import chain


# DFS function to generate all possible pairs
def generate_pairs_dfs(np_arr, duties, current_pair, valid_pairs, depth):
    if len(current_pair) == depth:
        valid_pairs.append(current_pair.copy())
        return

    for duty in [
        duties[i]
        for i in range(len(duties))
        if (np_arr[duties[i][0]][1] == np_arr[current_pair[-1][-1]][2])
        and (
            np_arr[duties[i][0]][3] - np_arr[current_pair[-1][-1]][4]
            >= np.timedelta64(12, "h")
            and (np_arr[duties[i][0]][3] - np_arr[current_pair[-1][-1]][4])
            <= np.timedelta64(14, "h")
        )
    ]:
        current_pair.append(duty)
        generate_pairs_dfs(np_arr, duties, current_pair, valid_pairs, depth)
        current_pair.pop()  # Backtrack


# Function to generate pairs
def generate_pairs(depth=3):
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
    for depth in range(2, depth + 1):
        for duty in duties:
            generate_pairs_dfs(np_arr, duties, [duty], valid_pair_dfs, depth)

    # save the pairings as a txt file
    with open(f"data/pairings/pairings.txt", "w") as file:
        file.writelines(f"{item}\n" for item in valid_pair_dfs)


def pairing_check():
    # Open the file in read mode
    with open("data/pairings/pairings.txt", "r") as file:
        lines = file.readlines()

    # convert each line (representing a list) to an actual list
    pairings = [eval(line) for line in lines]

    from itertools import chain

    pair = list(set(chain.from_iterable(chain.from_iterable(pairings))))
    print(len(pairings), len(pair))
