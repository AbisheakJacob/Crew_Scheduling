# importing the packages
import pandas as pd
import streamlit as st
from data.data_creation import create_data
from pairing_generation.duty_generation import generate_duties


# the code embeds the functions into a streamlit application
def main():
    # title of the web application
    st.title("Pairing Generation")

    # Upload CSV file through Streamlit
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Display the original DataFrame
        st.subheader("Original Data:")
        st.write(df)

        # call the function to generate the duties and pairings
        # generate_duties()
        # generate_pairs()

        # Display the generated duties
        st.subheader("Generated Duties:")
        # Open the file in read mode
        with open("data/duties/duties.txt", "r") as file:
            lines = file.readlines()

        # convert each line (representing a list) to an actual list
        duties = [eval(line) for line in lines]
        st.write(duties)

        # Display the generated pairings
        st.subheader("Generated Pairings List and Pairings Matrix:")
        # Open the file in read mode
        with open("data/pairings/pairings.txt", "r") as file:
            lines = file.readlines()

        # convert each line (representing a list) to an actual list
        pairings_list = [eval(line) for line in lines]
        st.write(pairings_list)
        # read the pairings matrix
        pairings = pd.read_csv("data/pairings/pair_matrix.csv")
        st.write(pairings)

        # Display the cost matrix
        st.subheader("Cost Matrix:")
        # read the pairings matrix
        cost_matrix = pd.read_csv("data/cost_matrix/cost_matrix.csv")
        st.write(cost_matrix)

        # Save the processed DataFrame to a new CSV file
        st.markdown(
            f"### Download Pairings Matrix CSV File\n"
            f"Click below to download the Generated Pair Matrix  as a CSV file."
        )
        st.download_button(
            label="Download CSV",
            data=pairings.to_csv(index=False).encode("utf-8"),
            key="download_button",
        )


if __name__ == "__main__":
    main()
