# generate duties

# importing the packages
import pandas as pd
from datetime import datetime, timedelta


def generate_duties_dfs(df, current_duty, valid_duty):
    # Recursive DFS for each remaining flight leg
    if is_valid_duty(df, current_duty):
        valid_duty.append(current_duty.copy())
        return
    if len(current_duty) == 3:
        return

    # Recursive DFS for each remaining flight leg
    for flight_leg_id in df["flight_leg_id"]:
        # Check if the leg can be added to the current pair
        # if is_valid_duty(df, current_duty.copy() + [flight_leg_id]):
        current_duty.append(flight_leg_id)
        generate_duties_dfs(df, current_duty, valid_duty)
        current_duty.pop()  # Backtrack


def is_valid_duty(df, current_duty):
    # Implement conditions for pair validity
    # Ensure matching destination and departure airports, and time gaps
    if len(current_duty) == 2:
        return (
            (
                df.loc[
                    df["flight_leg_id"] == current_duty[-1], "destination_airport"
                ].values[0]
                == df.loc[
                    df["flight_leg_id"] == current_duty[0], "departure_airport"
                ].values[0]
            )
            and (
                datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == current_duty[-1], "start_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
                - datetime.strptime(
                    df.loc[df["flight_leg_id"] == current_duty[0], "end_time"].values[
                        0
                    ],
                    "%Y-%m-%d %H:%M:%S",
                )
            )
            >= timedelta(hours=1)
            and (
                df.loc[
                    df["flight_leg_id"] == current_duty[0], "destination_airport"
                ].values[0]
                == df.loc[
                    df["flight_leg_id"] == current_duty[-1], "departure_airport"
                ].values[0]
            )
        )
    elif len(current_duty) == 3:
        return (
            (
                df.loc[
                    df["flight_leg_id"] == current_duty[-1], "destination_airport"
                ].values[0]
                == df.loc[
                    df["flight_leg_id"] == current_duty[0], "departure_airport"
                ].values[0]
            )
            and (
                datetime.strptime(
                    df.loc[df["flight_leg_id"] == current_duty[1], "start_time"].values[
                        0
                    ],
                    "%Y-%m-%d %H:%M:%S",
                )
                - datetime.strptime(
                    df.loc[df["flight_leg_id"] == current_duty[0], "end_time"].values[
                        0
                    ],
                    "%Y-%m-%d %H:%M:%S",
                )
            )
            >= timedelta(hours=1)
            and (
                datetime.strptime(
                    df.loc[
                        df["flight_leg_id"] == current_duty[-1], "start_time"
                    ].values[0],
                    "%Y-%m-%d %H:%M:%S",
                )
                - datetime.strptime(
                    df.loc[df["flight_leg_id"] == current_duty[1], "end_time"].values[
                        0
                    ],
                    "%Y-%m-%d %H:%M:%S",
                )
            )
            >= timedelta(hours=1)
            and (
                df.loc[
                    df["flight_leg_id"] == current_duty[0], "destination_airport"
                ].values[0]
                == df.loc[
                    df["flight_leg_id"] == current_duty[1], "departure_airport"
                ].values[0]
            )
            and (
                df.loc[
                    df["flight_leg_id"] == current_duty[1], "destination_airport"
                ].values[0]
                == df.loc[
                    df["flight_leg_id"] == current_duty[-1], "departure_airport"
                ].values[0]
            )
        )
    else:
        return False


def generate_duties():
    # reading the dataframe
    df = pd.read_csv("data/flight_legs/data.csv")
    df = df.head(50)
    # df["start_time"] = pd.to_datetime(df["start_time"], format="%Y-%m-%d %H:%M:%S")
    # df["end_time"] = pd.to_datetime(df["end_time"], format="%Y-%m-%d %H:%M:%S")
    # Initialize
    valid_duty_dfs = []

    # Start DFS from each flight leg
    for start_leg in df["flight_leg_id"]:
        generate_duties_dfs(df, [start_leg], valid_duty_dfs)

    # Open the file in write mode
    with open(f"data/duties/duties.txt", "w") as file:
        # Write each item in the list to a new line
        for item in valid_duty_dfs:
            file.write(f"{item}\n")
