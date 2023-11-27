# generate pairings

# importing the packages
import pandas as pd
from datetime import datetime, timedelta


def generate_pairs_dfs(df, duties, current_pair, valid_pairs):
    # Recursive DFS for each remaining flight leg
    if is_valid_pair(df, current_pair):
        valid_pairs.append(current_pair.copy())
        return
    if len(current_pair) == 3:
        return

    # Recursive DFS for each remaining flight leg
    for duty in duties:
        # Check if the leg can be added to the current pair
        # if is_valid_pair(df, current_pair.copy() + [flight_leg_id]):
        current_pair.append(duty)
        generate_pairs_dfs(df, duties, current_pair, valid_pairs)
        current_pair.pop()  # Backtrack


def is_valid_pair(df, current_pair):
    # Implement conditions for pair validity
    # Ensure matching destination and departure airports, and time gaps
    if len(current_pair) == 2:  # that is the number of duties
        return (
            df.loc[
                df["flight_leg_id"] == current_pair[-1][0], "destination_airport"
            ].values[0]
            == df.loc[
                df["flight_leg_id"] == current_pair[0][-1], "departure_airport"
            ].values[0]
        ) and (
            datetime.strptime(
                df.loc[df["flight_leg_id"] == current_pair[-1][0], "start_time"].values[
                    0
                ],
                "%Y-%m-%d %H:%M:%S",
            )
            - datetime.strptime(
                df.loc[df["flight_leg_id"] == current_pair[0][-1], "end_time"].values[
                    0
                ],
                "%Y-%m-%d %H:%M:%S",
            )
        ) >= timedelta(
            hours=2
        )
    elif len(current_pair) == 3:
        return (
            (
                datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == current_pair[1][0], "start_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
                - datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == current_pair[0][-1], "end_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
            )
            >= timedelta(hours=2)
            and (
                datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == current_pair[-1][0], "start_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
                - datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == current_pair[1][-1], "end_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
            )
            >= timedelta(hours=2)
            and (
                df.loc[
                    df["flight_leg_id"] == current_pair[0][-1], "destination_airport"
                ].values[0]
                == df.loc[
                    df["flight_leg_id"] == current_pair[1][0], "departure_airport"
                ].values[0]
            )
            and (
                df.loc[
                    df["flight_leg_id"] == current_pair[1][-1], "destination_airport"
                ].values[0]
                == df.loc[
                    df["flight_leg_id"] == current_pair[-1][0], "departure_airport"
                ].values[0]
            )
        )
    else:
        return False


def generate_pairs():
    # reading the dataframe
    df = pd.read_csv("../data/flight_legs/data.csv")
    df = df.head(50)
    # df["start_time"] = pd.to_datetime(df["start_time"], format="%Y-%m-%d %H:%M:%S")
    # df["end_time"] = pd.to_datetime(df["end_time"], format="%Y-%m-%d %H:%M:%S")
    # Initialize
    # read the pairs as list of lists
    # Open the file in read mode
    with open("../data/duties/duties.txt", "r") as file:
        lines = file.readlines()

    # convert each line (representing a list) to an actual list
    duties = [eval(line) for line in lines]

    # create a list to hold the valid pairs
    valid_pair_dfs = []

    # call the function to generate pairs
    for duty in duties:
        generate_pairs_dfs(df, duties, [duty], valid_pair_dfs)

    print(valid_pair_dfs)
