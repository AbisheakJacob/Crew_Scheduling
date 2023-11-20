# importing the packages
import pandas as pd
import random

def create_data(days, num_flights):
    
    # create a loop to create the excel sheets for a month
    for j in range(1, days + 1):

        # define the airports
        airports = ['Chennai', 'Bangalore', 'Mumbai', 'Delhi', 'Calcutta']

        # create a dictionary with the distance between each airport
        time_distance = {
            ('Chennai', 'Bangalore'): 1,
            ('Chennai', 'Mumbai'): 2,
            ('Chennai', 'Delhi'): 3,
            ('Chennai', 'Calcutta'): 2,
            ('Bangalore', 'Mumbai'): 1,
            ('Bangalore', 'Delhi'): 2,
            ('Bangalore', 'Calcutta'): 3,
            ('Mumbai', 'Delhi'): 2,
            ('Mumbai', 'Calcutta'): 3,
            ('Delhi', 'Calcutta'): 2
        }

        # create an empty list to hold flight legs
        flight_legs = []

        # Generate flight legs data
        for i in range(num_flights):
            departure_airport = random.choice(airports)
            destination_airport = departure_airport

            # Ensure different departure and destination airports
            while destination_airport == departure_airport:
                destination_airport = random.choice(airports)

            # get a random integer between 1 and 20 as the start time
            try:
                start_time = random.randint(1,20)
                end_time = start_time + time_distance[(departure_airport, destination_airport)]
            except:
                start_time = random.randint(1,20)
                end_time = start_time + time_distance[(destination_airport, departure_airport)]

            flight_legs.append({
                'flight_leg_id': i + 1,
                'departure_airport': departure_airport,
                'destination_airport': destination_airport,
                'start_time': start_time,
                'end_time': end_time
            })

        # Create a DataFrame from the generated data
        df = pd.DataFrame(flight_legs)

        df.to_csv(f"data/flight_legs/data_{j}.csv", index=False)