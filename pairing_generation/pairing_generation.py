# generate pairings

# importing the packages
import pandas as pd
from datetime import datetime, timedelta


def generate_pairs_dfs(df, duties, current_pair, valid_pairs):
    # Recursive DFS for each remaining flight leg
    if is_valid_pair(df, current_pair):
        valid_pairs.append(current_pair.copy())
        return
    if len(current_pair) == 5:
        return

    # Recursive DFS for each remaining flight leg
    for duty in [slist for slist in duties if (df.loc[df["flight_leg_id"] == current_pair[-1][-1], "destination_airport"].values[0] == df.loc[df["flight_leg_id"] == slist[0], "departure_airport"].values[0])]:
        # Check if the leg can be added to the current pair
        if sub_df(df,current_pair, duty):
            current_pair.append(duty)
            generate_pairs_dfs(df, duties, current_pair, valid_pairs)
            current_pair.pop()  # Backtrack

# function taking care of the time constraint and total time constraint
def sub_df(df, current_pair, duty):
    return ((
                datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == duty[0], "start_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
                - datetime.strptime(
                    df.loc[df["flight_leg_id"] == current_pair[-1][-1], "end_time"].values[
                        0
                    ],
                    "%Y-%m-%d %H:%M:%S",
                )
            )
            >= timedelta(hours=10) and (
                datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == duty[0], "start_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
                - datetime.strptime(
                    df.loc[df["flight_leg_id"] == current_pair[-1][-1], "end_time"].values[
                        0
                    ],
                    "%Y-%m-%d %H:%M:%S",
                )
            )
            <= timedelta(hours=12))

def is_valid_pair(df, current_pair):
    # Implement conditions for pair validity
    # Ensure matching destination and departure airports, and time gaps
    if len(current_pair) >= 2:
        return (
            df.loc[
                df["flight_leg_id"] == current_pair[-1][0], "destination_airport"
            ].values[0]
            == df.loc[
                df["flight_leg_id"] == current_pair[0][-1], "departure_airport"
            ].values[0]
        )
    else:
        return False


def generate_pairs():
    # reading the dataframe
    df = pd.read_csv("data/flight_legs/data.csv")
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
        generate_pairs_dfs(df, duties, [duty], valid_pair_dfs)

        # Open the file in write mode
    with open(f"data/pairings/pairings.txt", "w") as file:
        # Write each item in the list to a new line
        for item in valid_pair_dfs:
            file.write(f"{item}\n")

    # convert the file to a binary matrix csv file
    # Create an empty dataframe for the pair matrix
    pair_matrix = pd.DataFrame(
        index=range(1, len(valid_pair_dfs) + 1), columns=df["flight_leg_id"]
    )

    # Fill the pair matrix based on flight leg combinations
    for i, pair in enumerate(valid_pair_dfs):
        for j, duty in enumerate(pair):
            pair_matrix.loc[i + 1, pair[0]] = 1
            pair_matrix.loc[i + 1, pair[1]] = 1
            pair_matrix.loc[i + 1, pair[-1]] = 1

    # Fill NaN values with 0
    pair_matrix = pair_matrix.fillna(0)

    # save the pair matrix as a csv filr
    pair_matrix.to_csv("data/pairings/pair_matrix.csv", index=False)

    # create a list to store the cost for the pairings
    cost_list = []

    # calculate the cost matrix from pair list
    for pair in valid_pair_dfs:
        cost_sec = datetime.strptime(
            df.loc[df["flight_leg_id"] == pair[-1][-1], "end_time"].values[0],
            "%Y-%m-%d %H:%M:%S",
        ) - datetime.strptime(
            df.loc[df["flight_leg_id"] == pair[0][0], "start_time"].values[0],
            "%Y-%m-%d %H:%M:%S",
        )

        # Extract hours from the time difference
        cost_hr = cost_sec.total_seconds() / 3600
        cost_hr = abs(cost_hr)

        cost_list.append(cost_hr)

    # create the cost matrix
    cost_matrix = pd.DataFrame(cost_list, columns=["cost"])

    # save the pair matrix as a csv filr
    cost_matrix.to_csv("data/cost_matrix/cost_matrix.csv", index=False)