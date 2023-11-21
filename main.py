# importing the packages
from data.data_creation import create_data
from pairing_generation.duty_generation import generate_duties


def main():
    # create the data for generating the pairs
    # inputs are (number_of_days, num_of_flight_legs_per_day)
    create_data()
    generate_duties()


if __name__ == "__main__":
    main()
