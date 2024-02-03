"""
This program is a Lists and Sets Application designed to present a menu of options including:
Displaying all States in Alphabetical order including thier Capital, population, and state flower.
Displaying a single State with the Capital, population, and an image of the State Flower.
Displaying a Bar Graph of the Top 5 States with the highest population.
It also has a function to update a States population. It will verify inputs are valid.

Developer: Brian Walters SDEV300/6380
Developed: January 31, 2024
"""
import sys
from io import BytesIO
import pandas as pd
import requests
import matplotlib.pyplot as plt
from PIL import Image
import textwrap

# Main ---------------------------------------------------------------
def main():
    """
    The main function to execute the Lists and Sets Application.
    """
    # Display Welcome message
    welcome()

    while True:
        # Call Menu Function to get user selection
        selection = menu()

        if selection == '5':
            # Exit the program
            exit_program()
        else:
            # Call the function corresponding to the user's selection
            out = get_selection(selection)

            # Display the out
            display_output(out)

# Lists --------------------------------------------------------------

# Replace 'FILE PATH' with the actual path to your Excel FILE
FILE_PATH = \
r'C:\Users\brian\1. School UMGC\3. Spring 2024\1. SDEV 300\Week 3\Assignments\FlowerImageMap.xlsx'

# Read the Excel sheet into a DataFrame
df = pd.read_excel(FILE_PATH)

# Extract relevant information from the DataFrame
states = df['STATE NAME'].tolist()
state_ab = df['STATE ABBREVIATION'].tolist()
capital = df['CAPITAL CITY'].tolist()
population = df['POPULATION'].tolist()
flowers = df['STATE FLOWER'].tolist()
flower_images = dict(zip(states, df['STATE FLOWER IMAGE URL'].tolist()))

# Create a dictionary to map lowercase names to indexes
state_index_map = {state.lower(): i for i, state in enumerate(states)}

# Create a dictionary to map lowercase abbreviations to indexes
abbr_index_map = {abbr.lower(): i for i, abbr in enumerate(state_ab)}

# Functions ----------------------------------------------------------

# Welcome
def welcome():
    """
    Display the welcome message.
    """
    print("Welcome to the US State Information Aplication.")
    print("Please make a selection from the menu or push 5 to exit.")

# Menu
def menu():
    """
    Display the menu and get user selection.
    Returns:
        str: User selection.
    """
    print(textwrap.dedent("""
        What would you like to display?

        1. Display all U.S. States in Alphabetical order along with the Capital, \
State Population, and Flower.
        2. Search for a specific state and display the appropriate Capital Name, \
State Population, and an image of the associated State Flower.
        3. Provide a Bar graph of the top 5 populated States showing their \
overall population.
        4. Update the overall state population for a specific state.
        5. Exit Program
    """))
    selection = input("Enter selection: ")

    # Validate user input
    if selection not in ['1', '2', '3', '4', '5']:
        print("\nInvalid input. Please enter a valid option (1 - 5).")
        return menu()

    return selection

# Call the Function that was selected
def get_selection(selection):
    """
    Call the function corresponding to the user's selection.
    Args:
        selection (str): User selection.
    Returns:
        str: out of the selected function.
    """
    out = "*" * 90
    if selection == '1':
        out = display_all_states()
    elif selection == '2':
        out = display_single_state()
    elif selection == '3':
        out = top_populated_states_bar_graph()
    elif selection == '4':
        out = state_population_update()
    return out

# Display All States, Capitals, State Population, and Flower
def display_all_states():
    """
    Display all U.S. States in alphabetical order along with the Capital,
    State Population, and Flower.
    Returns:
        str: Formatted string with the state information.
    """
    # Combine state information into a list of tuples
    state_info = list(zip(states, state_ab, capital, population, flowers))

    # Sort the list of tuples based on the first element (state name)
    state_info.sort(key=lambda x: x[0])

    out = f"{'State':<20} {'Abbreviation':<15} {'Capital':<20} \
{'Population':<15} {'Flower':<20}\n"
    out += "=" * 100 + "\n"

    for state, ab, cap, pop, flower in state_info:
        out += f" {state:<20} {ab:<15} {cap:<20} {pop:<15} {flower:<20}\n"

    return out

# Display a single State, Capital, State Population, and Flower
def display_single_state():
    """
    Display information for a specific state including Capital, 
    State Population, and an image of the State Flower.
    Returns:
        str: Formatted string with the state information.
    """
    user_input = input("\nEnter the state name or abbreviation to display: ").lower()

    # Check if the user_input is in either the names or abbreviations
    if user_input.lower() in state_index_map or user_input.lower() in abbr_index_map:
        # Check if the user_input is in the names
        if user_input.lower() in state_index_map:
            index = state_index_map[user_input.lower()]
        else:
            index = abbr_index_map[user_input.lower()]

        state_info = (states[index], state_ab[index], capital[index],
                      population[index], flowers[index])

        # Display the state information
        out = "State Information:\n"
        out += f"{'State':<20} {'Abbreviation':<15} {'Capital':<20} \
{'Population':<15} {'Flower':<20}\n"
        out += "=" * 100 + "\n"
        state, ab, cap, pop, flower = state_info
        out += f"{state:<20} {ab:<15} {cap:<20} {pop:<15} {flower:<20}\n"

        # Display the flower image
        if flower_images.get(states[index]):
            out += "\nState Flower Image:\n"
            display_flower_image(states[index])
        else:
            out += "\nState Flower Image: Not available\n"

    else:
        out = "State not found. Exiting to main menu."

    return out

# Display a bar graph of the top 5 populated States showing their overall population
def top_populated_states_bar_graph():
    """
    Display a bar graph of the top 5 populated States showing their overall population.
    Returns:
        str: Success message.
    """
    top_states = sorted(zip(states, population), key=lambda x: x[1], reverse=True)[:5]

    state_names, state_populations = zip(*top_states)

    plt.bar(state_names, state_populations)
    plt.xlabel("State")
    plt.ylabel("Population")
    plt.title("Top 5 Populated States")
    plt.show()

    out = "Bar graph displayed successfully."

    return out

# Update a State's population
def state_population_update():
    """
    Update the overall state population for a specific state.
    Returns:
        str: Success message or an error message.
    """
    user_input = input(textwrap.dedent("\nEnter the state name or abbreviation to \
update population: ")).lower()

    if user_input.lower() in state_index_map or user_input.lower() in abbr_index_map:
        if user_input.lower() in state_index_map:
            index = state_index_map[user_input.lower()]
        else:
            index = abbr_index_map[user_input.lower()]

        while True:
            new_population = input(f"\nEnter the new population for {states[index]}: ")

            try:
                new_population_value = int(new_population)
                try:
                    if new_population_value >= 0:
                        population[index] = new_population_value
                        out = f"Population for {states[index]} updated successfully \
updated to {population[index]}."
                        return out
                except ValueError:
                    print("\nInvalid population input. Please enter a non-negative \
integer.")
            except ValueError:
                print("\nInvalid population input. Please enter a valid integer.")
    else:
        out = "State not found. Exiting to the main menu."

    return out

# Display Flowers
def display_flower_image(state_name):
    """
    Display the image of the State Flower for a specific state.
    """
    # Get the image URL for the specified state
    image_url = flower_images[state_name]

    try:
        # Request the image from the URL with a timeout
        response = requests.get(image_url, timeout=10)  # Adjust the timeout value as needed
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Display the image using PIL
        image = Image.open(BytesIO(response.content))
        image.show()

    except requests.RequestException as e:
        print(f"\nFailed to retrieve the image. Error: {e}")
        print("Returning to the main menu.")
        return

# Output
def display_output(out):
    """
    Display the output with user information.
    """
    print("\n", out)

# Function to exit the program
def exit_program():
    """
    Exit the program and display a thank you message.
    """
    print("\nThanks for trying the Python SDEV300 Lab 3 Application.\n"
        "You have selected to exit the application. Have a nice day.\n")
    sys.exit()

# Execute -------------------------------------------------------------
main()
