# importing the packages
import numpy as np
import pandas as pd
from itertools import chain


def generate_pairs_dfs(np_arr, duties, current_pair, valid_pairs):
    # Recursive np_arrS for each remaining flight leg
    if is_valid_pair(np_arr, current_pair):
        valid_pairs.append(current_pair.copy())
        return
    if len(current_pair) == 2:
        return

    # Recursive np_arrS for each remaining flight leg
    for duty in [duties[i] for i in range(len(duties)) if
                 (np_arr[duties[i][0]][1] == np_arr[current_pair[-1][-1]][2]) and (
                         np_arr[duties[i][0]][3] - np_arr[current_pair[-1][-1]][4] >= np.timedelta64(10, 'h') and (
                         np_arr[duties[i][0]][3] - np_arr[current_pair[-1][-1]][4]) <= np.timedelta64(15,
                                                                                                      'h'))]:  # return to homebase condition
        # Check if the leg can be added to the current pair
        # if sub_np_arr(np_arr,current_pair, duty):
        current_pair.append(duty)
        generate_pairs_dfs(np_arr, duties, current_pair, valid_pairs)
        current_pair.pop()  # Backtrack


def is_valid_pair(np_arr, current_pair):
    # Implement conditions for pair validity
    # Ensure matching destination and departure airports, and time gaps
    if len(current_pair) >= 2:
        return ((np_arr[current_pair[-1][-1]][4] - np_arr[current_pair[0][0]][3]) >= np.timedelta64(18, 'h'))
    else:
        return False


def save_info(valid_pair_dfs, np_arr):
    # Open the file in write mode
    with open(f"data/pairings/pairings.txt", "w") as file:
        file.writelines(f"{item}\n" for item in valid_pair_dfs)

    # create a zero np_array
    pair_array = np.zeros((len(valid_pair_dfs), len(np_arr)))

    # fill the values of the flight legs in each pairing with 1
    for i, pair in enumerate(valid_pair_dfs):
        pair_array[i, list(chain.from_iterable(pair))] = 1

    # save the pair_array as a txt file
    np.savetxt("data/pairings/pair_array.txt", pair_array, fmt="%d", delimiter=",")

    # calculate the cost matrix from pair list
    cost_list = [abs((np_arr[pair[-1][-1]][4] - np_arr[pair[0][0]][3]).total_seconds() / 3600) for pair in
                 valid_pair_dfs]

    with open(f"data/cost_matrix/cost.txt", "w") as file:
        file.writelines(f"{item}\n" for item in cost_list)


def generate_pairs():
    # reading the dataframe
    df = pd.read_csv("data/flight_legs/data.csv")
    df['start_time'] = pd.to_datetime(df['start_time'], format="%Y-%m-%d %H:%M:%S")
    df['end_time'] = pd.to_datetime(df['end_time'], format="%Y-%m-%d %H:%M:%S")

    np_arr = df.to_numpy()

    # Initialize
    # read the pairs as list of lists
    # Open the file in read mode
    with open("data/duties/duties.txt", "r") as file:
        lines = file.readlines()

    # convert each line (representing a list) to an actual list
    duties = [eval(line) for line in lines]

    # create a list to hold the valid pairs
    valid_pair_dfs = []

    # call the function to generate pairs
    for duty in duties:
        generate_pairs_dfs(np_arr, duties, [duty], valid_pair_dfs)

    # save the information into respective files
    save_info(valid_pair_dfs, np_arr)