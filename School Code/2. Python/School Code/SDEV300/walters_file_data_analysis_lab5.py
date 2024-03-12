"""
This Python program allows users to perform data analysis on two 
different datasets: Population Data and Housing Data. It provides 
a user-friendly interface where users can select the dataset they 
want to analyze and then choose specific columns within that dataset 
for analysis. For each selected column, the program calculates and 
displays various statistics such as count, mean, standard deviation, 
minimum, and maximum values. Additionally, it generates a histogram 
to visualize the distribution of data within the selected column. 
Users can easily navigate through the menu options and return to 
the main menu at any time. This application leverages Python libraries 
such as Pandas, NumPy, and Matplotlib for efficient data handling and 
visualization.

Developer: Brian Walters SDEV300/6380
Developed: February 14, 2024
"""

import sys
import textwrap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """
    Load data from a CSV file into a Pandas DataFrame.

    Parameters:
        filename (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the data, or None if file not found.
    """
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def clean_data(filename, data_type):
    """
    Clean and validate the data from a CSV file.

    Parameters:
        filename (str): The path to the CSV file containing the data.
        data_type (str): Type of data ('population' or 'housing').

    Returns:
        pandas.DataFrame: The cleaned and validated DataFrame, or None if file not found.
    """
    # Load data from CSV file
    data = load_data(filename)

    if data is not None:
        if data_type == 'population':
            # Validate and clean population data
            data = clean_population_data(data)
        elif data_type == 'housing':
            # Validate and clean housing data
            data = clean_housing_data(data)

    return data

def clean_population_data(data):
    """
    Clean and validate population data.

    Parameters:
        data (pandas.DataFrame): Population data DataFrame.

    Returns:
        pandas.DataFrame: Cleaned and validated population data.
    """
        # Validate and clean columns
    # Convert 'Target Geo Id' and 'Target Geo Id2' to strings
    data['Target Geo Id'] = data['Target Geo Id'].astype(str)
    data['Target Geo Id2'] = data['Target Geo Id2'].astype(str)
    
    # Validate and clean columns
    # Target Geo Id should be 14 characters long
    data = data[data['Target Geo Id'].str.len() == 14]

    # Target Geo Id2 should be 5 characters long
    data = data[data['Target Geo Id2'].str.len() == 5]

    # Pop Apr 1 and Pop Jul 1 should not contain any negative numbers
    data = data[(data['Pop Apr 1'] >= 0) & (data['Pop Jul 1'] >= 0)]

    # Change Pop should be Pop Jul 1 - Pop Apr 1
    data['Change Pop'] = data['Pop Jul 1'] - data['Pop Apr 1']

    return data

def clean_housing_data(data):
    """
    Clean and validate housing data.

    Parameters:
        data (pandas.DataFrame): Housing data DataFrame.

    Returns:
        pandas.DataFrame: Cleaned and validated housing data.
    """
    # Filter out rows with invalid built years
    data = data[data['BUILT'] > 0]

    # Fix the age by subtracting built year from the current year
    current_year = pd.Timestamp.now().year
    data['AGE'] = current_year - data['BUILT']

    # Exclude rows with negative age values
    data = data[data['AGE'] >= 0]

    # Check and make sure there is not more bedrms than there are rooms
    data = data[data['BEDRMS'] <= data['ROOMS']]

    # Check nunits, weight, and utilities for negative and zero
    data = data[(data['NUNITS'] > 0) & (data['WEIGHT'] > 0) & (data['UTILITY'] > 0)]

    return data

# Function to handle user input errors
def get_valid_input(options):
    """
    Get valid input from the user.

    Parameters:
        options (list): List of valid options.

    Returns:
        str: Valid user input.
    """
    while True:
        user_input = input("\nEnter selection: ").strip().lower()
        if user_input in options:
            return user_input
        print("Invalid input. Please enter a valid option.")

# Function to display statistics
def display_statistics(column_data):
    """
    Display statistics for the selected column.

    Parameters:
        column_data (pandas.Series): Data for the selected column.
    """
    count = column_data.count()
    mean = round(np.mean(column_data), 1)
    std_dev = round(np.std(column_data), 1)
    minimum = np.min(column_data)
    maximum = np.max(column_data)

    print("The statistics for this column are:")
    print("Count =", count)
    print("Mean =", mean)
    print("Standard Deviation =", std_dev)
    print("Min =", minimum)
    print("Max =", maximum)

# Function to display histogram
def display_histogram(column_data, column_name):
    """
    Display histogram for the selected column.

    Parameters:
        column_data (pandas.Series): Data for the selected column.
        column_name (str): Name of the column.
    """
    plt.hist(column_data, bins=50, color='#008fd5', edgecolor='black')  # Narrower bars
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title(column_name)
    plt.show()

# Welcome
def welcome():
    """
    Display the welcome message.
    """
    print(textwrap.dedent("""Welcome to the Python Data Analysis App!\
This program allows you to analyze data from two different datasets: Population Data and Housing Data.\
You can select a dataset and then choose a specific column for analysis.\
For each column, the program calculates and displays various statistics, such as count, mean, standard \
deviation, minimum, and maximum values.\
Additionally, it generates a histogram to visualize the distribution of data within the selected 
column."""))

# Function to exit the program
def exit_program():
    """
    Exit the program and display a thank you message.
    """
    print("\nThanks for trying the Python SDEV300 Lab 5 Application.\n"
        "You have selected to exit the application. Have a nice day.\n")
    sys.exit()

# Main function
def main():
    """
    The main function to execute the application.
    """
    welcome()

    while True:
        print("\nSelect the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")

        selection = get_valid_input(['1', '2', '3'])

        if selection == '3':
            exit_program()
        elif selection == '1':
            analyze_population_data()
        elif selection == '2':
            analyze_housing_data()

# Function to analyze population data
def analyze_population_data():
    """
    Analyze population data.
    """
    # Full path to the Population Data file
    filename = \
        r"C:\Users\brian\1. School UMGC\3. Spring 2024\1. SDEV 300\Week 5\Assignments\PopChange.csv"

    #filename = "PopChange.csv"     # untag this if this file is in the correct directory
    data = load_data(filename)

    if data is None:
        print("Population Data file not found.")
        return  # Exit the function if file not found

    # Clean and validate population data
    data = clean_population_data(data)

    print("\nYou have entered Population Data.")
    while True:
        print("\nSelect the Column you want to analyze:")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")

        selection = get_valid_input(['a', 'b', 'c', 'd'])

        if selection == 'd':
            break

        column_name = ""
        if selection == 'a':
            column_name = 'Pop Apr 1'
        elif selection == 'b':
            column_name = 'Pop Jul 1'
        elif selection == 'c':
            column_name = 'Change Pop'

        try:
            print("\nYou selected", column_name)
            column_data = data[column_name]
            display_statistics(column_data)
            display_histogram(column_data, column_name)
        except KeyError:
            print("Invalid column name.")

# Function to analyze housing data
def analyze_housing_data():
    """
    Analyze housing data.
    """
    # Full path to the Housing Data file
    filename = \
        r"C:\Users\brian\1. School UMGC\3. Spring 2024\1. SDEV 300\Week 5\Assignments\Housing.csv"

    #filename = "Housing.csv"    # untag this if this file is in the correct directory
    data = load_data(filename)

    if data is None:
        print("Housing Data file not found.")
        return  # Exit the function if file not found

    # Clean and validate housing data
    data = clean_housing_data(data)

    print("\nYou have entered Housing Data.")
    while True:
        print("\nSelect the Column you want to analyze:")
        print("a. Age")
        print("b. Bedrooms")
        print("c. Built")
        print("d. Rooms")
        print("e. Utility")
        print("f. Exit Column")

        selection = get_valid_input(['a', 'b', 'c', 'd', 'e', 'f'])

        if selection == 'f':
            break

        column_name = ""
        if selection == 'a':
            column_name = 'AGE'
        elif selection == 'b':
            column_name = 'BEDRMS'
        elif selection == 'c':
            column_name = 'BUILT'
        elif selection == 'd':
            column_name = 'ROOMS'
        elif selection == 'e':
            column_name = 'UTILITY'

        try:
            print("\nYou selected", column_name)
            column_data = data[column_name]
            display_statistics(column_data)
            display_histogram(column_data, column_name)
        except KeyError:
            print("Invalid column name.")

if __name__ == "__main__":
    main()
