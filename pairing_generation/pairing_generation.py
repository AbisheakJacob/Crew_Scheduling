# generate duties

# importing the packages
import pandas as pd
import os

def generate_pairs_dfs(df, current_pair, valid_pairs):
    # Base case: If the current pair is complete, add it to the list of valid pairs
    if len(current_pair) == 3:
        valid_pairs.append(current_pair.copy())
        return

    # Recursive DFS for each remaining flight leg
    for flight_leg_id in df['flight_leg_id']:
        # Check if the leg can be added to the current pair
        if is_valid_pair(df, current_pair, flight_leg_id):
            current_pair.append(flight_leg_id)
            generate_pairs_dfs(df, current_pair, valid_pairs)
            current_pair.pop()  # Backtrack

def is_valid_pair(df, current_pair, flight_leg_id):
    # Implement conditions for pair validity
    # Ensure matching destination and departure airports, and time gaps
    return (
        len(current_pair) == 0 or
        (df.loc[df['flight_leg_id'] == current_pair[-1], 'destination_airport'].values[0] ==
         df.loc[df['flight_leg_id'] == flight_leg_id, 'departure_airport'].values[0]) and
        (df.loc[df['flight_leg_id'] == flight_leg_id, 'start_time'].values[0] -
         df.loc[df['flight_leg_id'] == current_pair[-1], 'end_time'].values[0]) >= 1
    )

def generate_duties():
    
    # determine the directory where the files are located
    directory = 'data/flight_legs'

    for filename in os.listdir(directory):

        # reading the dataframe
        df = pd.read_csv(directory + "/" + filename)
        df = df.head(100)
        # Initialize
        valid_pairs_dfs = []

        # Start DFS from each flight leg
        for start_leg in df['flight_leg_id']:
            generate_pairs_dfs(df, [start_leg], valid_pairs_dfs)

        # Create an empty dataframe for the pair matrix
        pair_matrix_dfs = pd.DataFrame(index=range(1, len(valid_pairs_dfs) + 1), columns=df['flight_leg_id'])

        # Fill the pair matrix based on flight leg combinations
        for i, pair in enumerate(valid_pairs_dfs):
            for leg in pair:
                pair_matrix_dfs.loc[i+1, leg] = 1

        # Fill NaN values with 0
        pair_matrix_dfs = pair_matrix_dfs.fillna(0)

        # save the files in directories
        pair_matrix_dfs.to_csv(f"duty_{filename}", index=False)

