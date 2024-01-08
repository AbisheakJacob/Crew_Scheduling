# importing the packages
import numpy as np
import pandas as pd
import time
import streamlit as st
from data.data_creation import create_data
from pairing_generation.duty_generation import generate_duties
from pairing_generation.pairing_generation import generate_pairs
from crew_pairing.column_gen import column_gen
from timeit import default_timer as timer


# function to generate duties and pairs
def generate():
    # read the created data
    df = pd.read_csv("data/flight_legs/data.csv")
    # display the data
    st.subheader("Flight Legs Data:")

    # create a radio button to display the data
    data_option = st.radio("Display Data", ("Do Not Display", "Head", "Tail", "All"))

    # if user selects Do Not Display
    if data_option == "Do Not Display":
        pass
    # if user selects Head
    elif data_option == "Head":
        st.write(df.head())
    # if user selects Tail
    elif data_option == "Tail":
        st.write(df.tail())
    # if user selects All
    elif data_option == "All":
        st.write(df)

    # create a button to generate duties
    if st.button("Generate Duties"):
        # call the generate duties function inside a spinner
        with st.spinner("Generating Duties..."):
            generate_duties()

        # display the success message once the previous function is completed
        st.success("Duties Generated Successfully!")

    # create a button to generate pairs
    if st.button("Generate Pairs"):
        # call the generate pairs function inside a spinner
        with st.spinner("Generating Pairings..."):
            generate_pairs()

        # display the success message
        st.success("Pairings Generated Successfully!")

    # create a button to solve the problem using column gen
    if st.button("Solve Using Column Generation"):
        # call the column generation function inside a spinner
        with st.spinner("Solving Problem..."):
            column_gen()

        # display the success message
        st.success("Problem Solved Successfully!")


# the code embeds the functions into a streamlit application
def main():

    # title of the web application
    st.title("Pairing Generation")

    # select box to select the mode of selecting the dataset
    mode = st.selectbox("Select the mode of data selection", ("Upload", "Generate"))

    # if the user selects the upload mode
    if mode == "Upload":
        # Upload CSV file through Streamlit
        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
        if uploaded_file is not None:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(uploaded_file)
            df.to_csv("data/flight_legs/data.csv", index=False)

            generate()
    # if the user selects the generate mode
    elif mode == "Generate":
        # call the create duties function
        create_data()


# call the main function with the initiation of the file
if __name__ == "__main__":

    start = timer()
    main()
    print(timer()-start)
