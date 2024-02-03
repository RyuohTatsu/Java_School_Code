"""
This program is a Math Secrets Application designed to present a menu of options including:
Generating a secure password, Calculating and formatting a percentage, telling the user
how many days left until July 4, 2025, Using the law of Cosines to calculate the leg of a triangle,
and Calculating the volume of a Right Circular Cylinder. It will verify inputs are valid.

Developer: Brian Walters SDEV300/6380
Developed: January 24, 2024
"""

import sys
import datetime
import math
import secrets
import string

# Constants
BORDER_LENGTH = 90

# Main ---------------------------------------------------------------
def main():
    """
    The main function to execute the Math Secrets Application.
    """
    # Display Welcome message
    welcome()

    while True:
        # Call Menu Function to get user selection
        selection = menu()

        if selection == 'f':
            # Exit the program
            exit_program()
        else:
            # Call the function corresponding to the user's selection
            result = get_selection(selection)

            # Display the result
            display_output(result)

# Functions -----------------------------------------------------------------

# Welcome ------------------------------
def welcome():
    """
    Display the welcome message.
    """
    print("\nWelcome to the Python SDEV300 Lab 2 Application.")
    print("Please choose an option from the menu and input the "
          "information requested to see the results.")

# Menu -------------------------------------------
def menu():
    """
    Display the menu and get user selection.
    Returns:
        str: User selection.
    """
    print("\nWhat would you like to do today?")
    print("\ta. Generate a Secure Password")
    print("\tb. Calculate and format a percentage")
    print("\tc. How many days from today until July 4, 2025?")
    print("\td. Use the Law of Cosines to calculate the leg of a triangle")
    print("\te. Calculate the volume of a Right Circular Cylinder")
    print("\tf. Exit Program")
    selection = input("Enter selection:  ")

    # Validate user input
    if selection.lower() not in ['a', 'b', 'c', 'd', 'e', 'f']:
        error = "Invalid input. Please enter a valid option (a - f)."
        print_error_message(error)

    return selection

# Call the Function that was selected --------------------------
def get_selection(selection):
    """
    Call the function corresponding to the user's selection.
    Args:
        selection (str): User selection.
    Returns:
        str: Result of the selected function.
    """
    result = "*" * BORDER_LENGTH
    if selection == 'a':
        result = generate_password()
    elif selection == 'b':
        result = calculate_percentage()
    elif selection == 'c':
        result = calculate_days_until_july_4()
    elif selection == 'd':
        result = calculate_triangle_leg()
    elif selection == 'e':
        result = calculate_cylinder_volume()
    return result

# Generate a Secure Password ----------------------
def generate_password():
    """
    Generate a secure password based on user input.
    Returns:
        str: Generated password.
    """
    # Set Minimum Required
    min_length = 5
    min_uppercase = 1
    min_lowercase = 1
    min_digits = 1
    min_special_chars = 1

    # Ask user for password parameters
    length = get_positive_integer_input(f"How long should the password be? (Minimum {min_length}): ")
    uppercase = get_positive_integer_input(f"Minimum number of upper case characters? (Minimum {min_uppercase}): ")
    lowercase = get_positive_integer_input(f"Minimum number of lower case characters? (Minimum {min_lowercase}): ")
    digits = get_positive_integer_input(f"Minimum number of digit characters? (Minimum {min_digits}): ")
    special_chars = get_positive_integer_input(f"Minimum number of special characters? (Minimum {min_special_chars}): ")

    # Validate input
    if (
        length < min_length
        or uppercase < min_uppercase
        or lowercase < min_lowercase
        or digits < min_digits
        or special_chars < min_special_chars
    ):
        error = "Input constraints do not meet minimum requirements."
        print_error_message(error)
        return "Password generation aborted."

    # Validate overall length
    if length < uppercase + lowercase + digits + special_chars:
        error = "Input constraints exceed password length."
        print_error_message(error)
        return "Password generation aborted."

    # Calculate the remaining characters for lowercase
    remaining_lowercase = max(0, length - uppercase - digits - special_chars)

    # Generate password
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password_list = [secrets.choice(string.ascii_uppercase) for _ in range(uppercase)]
    password_list += [secrets.choice(string.ascii_lowercase) for _ in range(lowercase)]
    password_list += [secrets.choice(string.digits) for _ in range(digits)]
    password_list += [secrets.choice(string.punctuation) for _ in range(special_chars)]
    password_list += [secrets.choice(chars) for _ in range(remaining_lowercase)]

    # Shuffle the password characters
    secrets.SystemRandom().shuffle(password_list)

    # Trim the password to the specified length
    generated_password = ''.join(password_list)[:length]

    return f"Password Generated: {generated_password}"

# Calculate and Format a Percentage --------------------
def calculate_percentage():
    """
    Calculate and format a percentage based on user input.
    Returns:
        str: Formatted percentage.
    """
    # Ask user for percentage parameters
    numerator = get_positive_integer_input("Enter a positive integer numerator: ")
    denominator = get_positive_integer_input("Enter a positive integer denominator: ")
    precision = get_positive_integer_input("Enter the number of decimal places: ")

    # Validate input
    if denominator == 0:
        error = "Denominator cannot be zero."
        print_error_message(error)
        return "Calculate and Format a Percentage aborted."

    # Calculate percentage
    percent = (numerator / denominator) * 100

    # Format percentage
    formatted_percent = f"{numerator} / {denominator} yields {percent:.{precision}f} percent"

    return formatted_percent

# How Many Days until July 4, 2025 ---------------------
def calculate_days_until_july_4():
    """
    Calculate the number of days until July 4, 2025.
    Returns:
        str: Formatted result with days remaining.
    """
    # Calculate days remaining
    target_date = datetime.date(2025, 7, 4)
    today = datetime.date.today()
    days_remaining = (target_date - today).days

    return f"{days_remaining} days until target date {target_date.strftime('%a %b %d, %Y')}"

# Use the Law of Cosines to Calculate the leg of a Triangle ----
def calculate_triangle_leg():
    """
    Use the Law of Cosines to calculate the leg of a triangle based on user input.
    Returns:
        str: Resulting length of the triangle leg.
    """
    # Ask user for triangle parameters
    a = get_positive_float_input("Enter a positive number for line a <-> c length: ")
    b = get_positive_float_input("Enter a positive number for line c <-> b length: ")
    angle_c = get_positive_float_input("Enter a positive number for angle of C in the "
                                        "triangle (in degrees): ")

    # Validate input
    if a <= 0 or b <= 0 or angle_c <= 0:
        error = "All inputs must be positive values."
        print_error_message(error)
        return "Use the Law of Cosines to Calculate the leg of a Triangle aborted."

    # Convert angle to radians
    angle_c_rad = math.radians(angle_c)

    # Calculate the length of the triangle leg using the Law of Cosines
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_c_rad))

    return f"The length of line c is: {c:.2f}"

# Calculate the Volume of a Right Circle Cylinder ----------
def calculate_cylinder_volume():
    """
    Calculate the volume of a right circular cylinder based on user input.
    Returns:
        str: Resulting volume of the cylinder.
    """
    # Ask user for cylinder parameters
    radius = get_positive_float_input("Enter a positive number for the "
                                        "radius of the cylinder: ")
    height = get_positive_float_input("Enter a positive number for the "
                                        "height of the cylinder: ")

    # Validate input
    if radius <= 0 or height <= 0:
        error = "Both radius and height must be positive values."
        print_error_message(error)
        return "Calculate the Volume of a Right Circle Cylinder aborted."

    # Calculate the volume of the cylinder
    volume = math.pi * radius**2 * height

    return f"The volume of the Right Circular Cylinder is: {volume:.5f}"

# Helper function to get positive integer input ----------------
def get_positive_integer_input(prompt):
    """
    Get positive integer input from the user.
    Returns:
        int: Positive integer entered by the user.
    """
    value = -1
    while value < 0:
        try:
            value = int(input(prompt))
            if value < 0:
                error = "Invalid input. Please enter a positive integer."
                print_error_message(error)
        except ValueError:
            error = "Invalid input. Please enter a valid integer."
            print_error_message(error)
    return value

# Helper function to get positive float input -------------------
def get_positive_float_input(prompt):
    """
    Get positive float input from the user.
    Returns:
        float: Positive float entered by the user.
    """
    value = -1
    while value < 0:
        try:
            value = float(input(prompt))
            if value < 0:
                error = "Invalid input. Please enter a positive number."
                print_error_message(error)
        except ValueError:
            error = "Invalid input. Please enter a valid number."
            print_error_message(error)
    return value

# Output ------------------------------------------
def display_output(result):
    """
    Display the output with user information.
    """
    print(f"\n{'*' * BORDER_LENGTH}\n{result}\n{'*' * BORDER_LENGTH}")

# Function to exit the program ----------------------
def exit_program():
    """
    Exit the program and display a thank you message.
    """
    message = (
        "Thanks for trying the Python SDEV300 Lab 2 Application.\n"
        "You have selected to exit the application. Have a nice day."
    )
    display_output(message)
    sys.exit()

# Function to print error messages -------------------
def print_error_message(error):
    """
    Print an error message.
    """
    formatted_error = f"Error: {error}"
    display_output(formatted_error)

# Execute ---------------------------------------------------------------------
main()
