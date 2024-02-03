"""
This program converts temperatures from Fahrenheit to Celsius.

Developer: Brian Walters SDEV300/6380
Developed: January 27, 2024
"""
def main():
    """
    Main function to take user input for a temperature in Fahrenheit,
    convert it to Celsius, and print the result.

    Parameters:
    None

    Returns:
    None
    """
    while True:
        try:
            fahrenheit = int(input("Enter a temperature value in Fahrenheit.\n"))
            break
        except ValueError:
            print("\nPlease enter a whole number.\n")

    celsius = round((fahrenheit - 32) / 1.8, 1)

    print("The conversion of", fahrenheit, "Fahrenheit is", celsius, "Celsius.")

# Execute the main function
main()
