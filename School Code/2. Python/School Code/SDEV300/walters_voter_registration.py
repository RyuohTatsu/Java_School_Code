"""
This program is a Voter Registration Application designed to get first and last name,
age, U.S. Citizen Status, State of Residence, and Zip Code. It will verify inputs are valid.

Developer: Brian Walters SDEV300/6380
Developed: January 12, 2024
"""
import sys

# Main ---------------------------------------------------------------
def main():
    """
    The main function to execute the Voter Registration Application.
    """
    # Display Welcome message
    welcome()

    # Call Functions
    user_info = get_user_info()

    # Display output
    display_output(user_info)

# Functions ----------------------------

# Welcome ------------------------------
def welcome():
    """
    Display the welcome message.
    """
    print("\nWelcome to the Python Voter Registration Application")
    print("Fill in all fields.")
    print("You can exit this application at any time by entering 'q' in any field.")

# Get User Info -----------------------------
def get_user_info():
    """
    Prompt the user to enter their information.
    """
    user_info = {
        "first_name": ask_name("First Name"),
        "last_name": ask_name("Last Name"),
        "age": ask_age(),
        "citizen_status": ask_citizen(),
        "state": ask_state(),
        "zip_code": ask_zip_code()
    }
    return user_info

# Ask Name -------------------------------------
def ask_name(name_type):
    """
    Prompt the user to enter their first or last name.
    """
    print("\nEnter 'q' to exit the application.")
    name = input(f"Please enter your {name_type}:\t")

    # If 'q' is entered, exit application.
    if name.lower() == 'q':
        exit_program()

    # If blank, reprompt
    while not name:
        print(f"\nInvalid input. Please enter your {name_type}.")
        print("Enter 'q' to exit the application.")
        name = input(f"Please enter your {name_type}:\t")
        if name.lower() == 'q':
            exit_program()

    return name

# Ask Age -----------------------------
def ask_age():
    """
    Prompt the user to enter their age.
    """
    while True:
        print("\nEnter 'q' to exit the application.")
        age = input("Please enter your Age:\t")

        # If 'q' is entered, exit application.
        if age.lower() == 'q':
            exit_program()

        # Check if it's not a valid integer
        if not age.isdigit():
            print("Invalid input. Please enter a valid age.")
            continue  # Skip the rest of the loop and start a new iteration

        age = int(age)

        # Check age conditions and print the appropriate message
        if 1 <= age <= 17:
            print("You are too young to vote. Exiting the application.")
            exit_program()
        elif 18 <= age <= 120:
            print("You are eligible to vote.")
            return age  # Exit the loop and return the valid age
        else:
            print("Invalid age. Please enter a valid age between 0 and 120.")

# Ask if US Citizen -----------------------------
def ask_citizen():
    """
    Prompt the user to enter their US citizenship status.
    """
    print("\nEnter 'q' to exit the application.")
    print("Are you a US Citizen?")
    citizen_status = input("Enter Yes or No:\t").lower()

    # If 'q' is entered, exit application.
    if citizen_status == 'q':
        exit_program()

    # If blank, reprompt
    while citizen_status not in ['yes', 'no']:
        print("\nInvalid input. Please enter Yes or No.")
        print("Enter 'q' to exit the application.")
        citizen_status = input("Enter Yes or No:\t").lower()
        if citizen_status == 'q':
            exit_program()

    if citizen_status == 'no':
        print("\nYou are not eligible to register to vote.")
        exit_program()

    return citizen_status

# Ask State -----------------------------
def ask_state():
    """
    Prompt the user to enter their state of residence.
    """
    # Make a dictionary of states to reference.
    print("\nEnter 'q' to exit the application.")
    state = input("Please enter your State of Residence (Ex. FL):\t")

    # If 'q' is entered, exit application.
    if state.lower() == 'q':
        exit_program()

    # If blank, reprompt
    while not state:
        print("\nInvalid input. Please enter your State of Residence.")
        print("Enter 'q' to exit the application.")
        state = input("Please enter your State of Residence (Ex. FL):\t")
        if state.lower() == 'q':
            exit_program()

    # Check input against a list of valid states. If not valid, reprompt.
    valid_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", \
                    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", \
                    "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", \
                    "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", \
                    "VA", "WA", "WV", "WI", "WY"]

    while state.upper() not in valid_states:
        print("\nInvalid state. Please enter a valid State abbreviation.")
        print("Enter 'q' to exit the application.")
        state = input("Please enter your State of Residence (Ex. FL):\t")
        if state.lower() == 'q':
            exit_program()

    return state

# Ask Zip Code -----------------------------
def ask_zip_code():
    """
    Prompt the user to enter their zip code.
    """
    # Zip code must be numbers and only 5 digits. If not valid, reprompt.
    print("\nEnter 'q' to exit the application.")
    zip_code = input("Please enter your Zip Code:\t")

    # If 'q' is entered, exit application.
    if zip_code.lower() == 'q':
        exit_program()

    # If blank or not a valid zip code, reprompt
    while not zip_code.isdigit() or len(zip_code) != 5:
        print("\nInvalid input. Please enter a valid 5-digit Zip Code.")
        print("Enter 'q' to exit the application.")
        zip_code = input("Please enter your Zip Code:\t")
        if zip_code.lower() == 'q':
            exit_program()

    return zip_code

# Function to exit the program
def exit_program():
    """
    Exit the program and display a thank you message.
    """
    print("\nExiting the application. Thank you!\n")
    sys.exit()

# Output ------------------------------------------
def display_output(user_info):
    """
    Display the output with user information.
    """
    print("\nThanks for registering to vote. Here is the information we received:")
    print("Name (First Last):", user_info["first_name"].upper(), user_info["last_name"].upper())
    print("Age:", user_info["age"])
    print("U.S. Citizen:", user_info["citizen_status"].upper())
    print("State:", user_info["state"].upper())
    print("Zip code:", user_info["zip_code"])
    print("\nThanks for trying the Voter Registration Application.\
          \nYour voter registration card should be shipped within 3 weeks.")
    exit_program()

# Execute -----------------------------------------------
main()
