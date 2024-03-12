"""
This program has a menu that allows the user to pick between a Matrix Game
and a Password Cracking Function.

The Matrix Game allows a user to enter and validate their phone number and 
zipcode+4. Then the user will enter values of two, 3x3 matrices and then 
select from options including, addition, subtraction, matrix multiplication, 
and element by element multiplication. The program will compute the appropriate 
results and return the results, the transpose of the results, the mean of the 
rows for the results, and the mean of the columns for the results.

The Password Cracking Function will give the user a choice to input a password
or generate a random password. It will then hash the passord with different 
hashing algorithms and display the hash.

Developer: Brian Walters SDEV300/6380
Developed: February 7, 2024
"""
import re
import secrets
import sys
import hashlib
import textwrap
import numpy as np

CHAR_SETS = {'UPPER_ALPHA': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'LOWER_ALPHA': 'abcdefghijklmnopqrstuvwxyz',
             'DIGITS': '0123456789',
             'SPECIAL': r'^!\$%&/()=?{[]}+~#-_.:,;<>|\\'}

# Main ---------------------------------------------------------------
def main():
    """
    The main function to execute the application.

    This function displays the welcome message and presents the user with a 
    menu to select different options.
    
    It continuously loops until the user chooses to exit the program.
    """
    # Display Welcome message
    welcome()

    while True:
        # Call Menu Function to get user selection
        selection = menu()

        if selection == '3':
            # Exit the program
            exit_program()
        elif selection == '1':
            # Play the Matrix Game
            matrix_operations = MatrixOperations()
            matrix_operations.run()
        elif selection == '2':
            # Create Hashed Passwords
            password_cracking = PasswordCracking()
            password_cracking.run()

# Menu Functions ----------------------------------------------------------
# Welcome
def welcome():
    """
    Display the welcome message.
    """
    print("\nWelcome to fun with numpy.\n")
    print(textwrap.dedent("""Option 1 the Matrix Game will allow you to enter and \
validate your phone number and zipcode+4. Then you will enter values of two, 3x3 matrices \
and then select from options including, addition, subtraction, matrix multiplication, \
and element by element multiplication. The program will compute the appropriate \
results and return the results, the transpose of the results, the mean of the \
rows for the results, and the mean of the columns for the results. \

Option 2 The Password Cracking Function will give you a choice to input a password \
or generate a random password. It will then hash the passord with different \
hashing algorithms and display the hashes for you to copy and try in an password cracking tool \
of your choice online."""))

# Menu
def menu():
    """
    Display the menu and get user selection.
    Returns:
        str: User selection.
    """
    print(textwrap.dedent("""
        What would you like to do?

        1. Play the Matrix Game?
        2. Create Hashed Passwords?
        3. Exit Program
    """))
    selection = input("Enter selection: ")

    # Validate user input
    if selection not in ['1', '2', '3']:
        print("\nInvalid input. Please enter a valid option (1 - 3).")
        return menu()

    return selection

# Function to exit the program
def exit_program():
    """
    Exit the program and display a thank you message.
    """
    print("\nThanks for trying the Python SDEV300 Lab 4 Application.\n"
        "You have selected to exit the application. Have a nice day.\n")
    sys.exit()

# Matrix Operations Class --------------------------------------------
class MatrixOperations:
    """
    A class to perform various matrix operations.

    ...

    Methods
    -------
    run():
        Run the matrix operations application.
    phone_number():
        Prompt the user to enter a phone number and validate its format.
    zip_code():
        Prompt the user to enter a zip code and validate its format.
    matrix():
        Prompt the user to enter values for two 3x3 matrices and validate them.
    choice():
        Prompt the user to select a matrix operation.
    get_type_pass(calculation_choice):
        Perform the selected matrix operation based on the user's choice.
    addition():
        Perform matrix addition.
    subtraction():
        Perform matrix subtraction.
    matrix_multiplication():
        Perform matrix multiplication.
    element_multiplication():
        Perform element-wise multiplication.

    Attributes:
        matrix1 (numpy.ndarray): The first 3x3 matrix.
        matrix2 (numpy.ndarray): The second 3x3 matrix.
    """

    def __init__(self):
        """
        Initializes the MatrixOperations class.
        """
        self.phonenumber = None
        self.zipcode = None
        self.matrix1 = None
        self.matrix2 = None

    def run(self):
        """
        Run the matrix operations application.
        """
        while True:
            self.phone_number()  # Prompt for phone number
            self.zip_code()      # Prompt for zip code
            self.matrix()        # Prompt for matrices
            self.choice()        # Prompt for matrix operation choice
            play_again = input("Do you want to play the Matrix Game again? (yes/no): ").lower()
            if play_again in ('yes', 'y'):
                # Loop back to play the game again
                continue
            else:
                exit_program()  # Exit the program

    def phone_number(self):
        """
        Prompt the user to enter a phone number and validate its format.
        """
        phonenumber = None
        phone_regex = r'^\(\d{3}\)\s?\d{3}-?\d{4}$'
        while phonenumber is None or not re.match(phone_regex, phonenumber):
            phonenumber = input("Enter your phone number (XXX) XXX-XXXX: ")
            if re.match(phone_regex, phonenumber):
                print(phonenumber, "is valid.")
                self.phonenumber = phonenumber  # Assign the validated phone number to the attribute
            else:
                print("Invalid phone number format. Please enter in the format (XXX) XXX-XXXX.")

    def zip_code(self):
        """
        Prompt the user to enter a zip code and validate its format.
        """
        zipcode = None
        zip_regex = r'^\d{5}-?\d{4}$'
        while zipcode is None or not re.match(zip_regex, zipcode):
            zipcode = input("Enter your zip code (XXXXX-XXXX): ")
            if re.match(zip_regex, zipcode):
                print(zipcode, "is valid.")
                self.zipcode = zipcode  # Assign the validated zip code to the attribute
            else:
                print("Invalid zip code format. Please enter in the format XXXXX-XXXX or XXXXX.")

    def matrix(self):
        """
        Prompt the user to enter values for two 3x3 matrices and validate them.
        """
        self.matrix1 = self.get_matrix("first")
        self.matrix2 = self.get_matrix("second")

    def get_matrix(self, ordinal):
        """
        Prompt the user to enter values for a 3x3 matrix and validate it.

        Parameters:
            ordinal (str): The ordinal indicator for the matrix (e.g., "first", "second").

        Returns:
            np.ndarray: A 3x3 matrix entered by the user.
        """
        while True:
            try:
                values = [int(x) for x in input(f"Enter values for the {ordinal} 3x3 matrix \
(space-separated values): ").split()]
                if len(values) != 9:
                    raise ValueError("Please enter 9 numeric values separated by spaces.")
                matrix = np.array(values).reshape(3, 3)
                print(f"Your {ordinal} 3x3 matrix is:")
                print(matrix)
                return matrix
            except ValueError as e:
                print(e)
                print("Invalid input. Please try again.")

    def choice(self):
        """
        Prompt the user to select a matrix operation.
        """
        print(textwrap.dedent("""
            Select a Matrix Operation from the list below:

            1. Addition
            2. Subtraction
            3. Matrix Multiplication
            4. Element by element multiplication
        """))
        calculation_choice = input("Enter selection: ")

        # Validate user input
        if calculation_choice not in ['1', '2', '3', '4']:
            print("\nInvalid input. Please enter a valid option (1 - 4).")
            return self.choice()

        return self.perform_operation(calculation_choice)

    def perform_operation(self, operation):
        """
        Perform the selected matrix operation based on the user's choice.

        Parameters:
            operation (str): The user's choice of matrix operation.
        """
        result = self.calculate_operation(operation)

        if result is not None:
            print("Calculation result:")
            print(result)

            # Transpose
            print("Transpose:")
            print(np.transpose(result))

            # Mean of rows
            mean_rows = np.mean(result, axis=1)
            print("Mean of rows:")
            print(np.round(mean_rows, 2))  # Round to two decimal places

            # Mean of columns
            mean_columns = np.mean(result, axis=0)
            print("Mean of columns:")
            print(np.round(mean_columns, 2))  # Round to two decimal places
        else:
            print("Error: Invalid operation.")

    def calculate_operation(self, operation):
        """
        Perform the selected matrix operation.

        Parameters:
            operation (str): The user's choice of matrix operation.

        Returns:
            np.ndarray or None: The result of the matrix operation, 
            or None if matrices are not initialized.

        Raises:
            ValueError: If the operation is invalid.
        """
        if operation == '1':
            return self.addition()
        if operation == '2':
            return self.subtraction()
        if operation == '3':
            return self.matrix_multiplication()
        if operation == '4':
            return self.element_multiplication()

        raise ValueError(f"Invalid operation: {operation}")

    def addition(self):
        """
        Perform matrix addition.

        Returns:
            np.ndarray: The result of matrix addition.
        """
        if self.matrix1 is not None and self.matrix2 is not None:
            result = self.matrix1 + self.matrix2
        else:
            print("Error: Matrices are not initialized.")
            return None
        return result

    def subtraction(self):
        """
        Perform matrix subtraction.

        Returns:
            np.ndarray: The result of matrix subtraction.
        """
        if self.matrix1 is not None and self.matrix2 is not None:
            result = self.matrix1 - self.matrix2
        else:
            print("Error: Matrices are not initialized.")
            return None
        return result

    def matrix_multiplication(self):
        """
        Perform matrix multiplication.

        Returns:
            np.ndarray: The result of matrix multiplication.
        """
        if self.matrix1 is not None and self.matrix2 is not None:
            result = np.matmul(self.matrix1, self.matrix2)
        else:
            print("Error: Matrices are not initialized.")
            return None
        return result

    def element_multiplication(self):
        """
        Perform element-wise multiplication.

        Returns:
            np.ndarray: The result of element-wise multiplication.
        """
        if self.matrix1 is not None and self.matrix2 is not None:
            result = self.matrix1 * self.matrix2
        else:
            print("Error: Matrices are not initialized.")
            return None
        return result

# Password Cracking Class --------------------------------------------
class PasswordCracking:
    """
    A class to handle password generation, input, hashing, and password cracking.

    ...

    Methods
    -------
    run():
        Run the password cracking application.
    choice():
        Prompt the user to select an action - generate a password or input a password.
    get_type_pass(type_pass):
        Perform the selected action based on the user's choice.
    generate_password():
        Generate a secure password with user-defined parameters.
    user_password():
        Prompt the user to input a password and validate it against predefined criteria.
    password_hash(raw_password):
        Hash the password using different algorithms.
    """

    def run(self):
        """
        Main function to execute password generation or input.
        """
        while True:
            self.choice()

    def choice(self):
        """
        Display the menu and get user selection.
        """
        print(textwrap.dedent("""
            What would you like to do?

            1. Generate Passwords
            2. Input Password
            3. Exit Program
        """))
        type_pass = input("Enter selection: ")

        # Validate user input
        if type_pass not in ['1', '2', '3']:
            print("\nInvalid input. Please enter a valid option (1 - 3).")
            return self.choice()

        if type_pass == '3':
            exit_program()

        return self.get_type_pass(type_pass)

    def get_type_pass(self, type_pass):
        """
        Call the corresponding function based on user input.
        """
        if type_pass == '1':
            raw_passwords = self.generate_password()
        elif type_pass == '2':
            raw_password = self.user_password()
            raw_passwords = [raw_password]
        else:
            return

        for raw_password in raw_passwords:
            print("Password:", raw_password)
            hashed_passwords = self.password_hash(raw_password)
            print("Hashed Passwords:")
            for hash_algorithm, hash_value in hashed_passwords.items():
                print(f"{hash_algorithm}: {hash_value}")
            print()

    def generate_password(self):
        """
        Generate a secure password with user-defined parameters.

        Returns:
            list: A list of generated passwords.
        """
        passwords = []

        for _ in range(10):
            length = secrets.randbelow(15) + 12  # Random length between 12 and 26
            unique_password = ''

            for _ in range(2):  # Fixed number of characters for each character type
                unique_password += secrets.choice(CHAR_SETS['UPPER_ALPHA'])
                unique_password += secrets.choice(CHAR_SETS['LOWER_ALPHA'])
                unique_password += secrets.choice(CHAR_SETS['DIGITS'])
                unique_password += secrets.choice(CHAR_SETS['SPECIAL'])

            # Pad in with the remaining random chars
            for _ in range(length - 8):  # Subtracting the fixed length from the total length
                char_type = secrets.choice(list(CHAR_SETS))
                unique_password += secrets.choice(CHAR_SETS[char_type])

            # Shuffle up the password to randomize the char sets
            password_list = list(unique_password)
            secrets.SystemRandom().shuffle(password_list)
            unique_password = ''.join(password_list)

            passwords.append(unique_password)

        return passwords

    def user_password(self):
        """
        Prompt the user to input a password and validate it against predefined criteria.

        Returns:
            str: The valid password entered by the user.
        """
        password = ''
        while password == '':
            try:
                user_password = input("Input a password of your choice: ")

                # Check if the password contains at least one character from each character set
                if (any(char in user_password for char in CHAR_SETS['UPPER_ALPHA']) and
                    any(char in user_password for char in CHAR_SETS['LOWER_ALPHA']) and
                    any(char in user_password for char in CHAR_SETS['DIGITS']) and
                    any(char in user_password for char in CHAR_SETS['SPECIAL'])):
                    password = user_password

                else:
                    raise ValueError("Invalid password format. Please make sure your password  "
                                    "contains at least one uppercase letter, one lowercase letter, "
                                    "one digit, and one special character.")
            except ValueError as e:
                print(f"Error: {e}")

        return password

    def password_hash(self, raw_password):
        """
        Hash the given raw password using different hashing algorithms.

        :param raw_password: The raw password to be hashed.
        :type raw_password: str
        :return: A dictionary containing the hashed passwords using various algorithms.
        :rtype: dict
        """
        md5_hash = hashlib.md5(raw_password.encode()).hexdigest()
        sha1_hash = hashlib.sha1(raw_password.encode()).hexdigest()
        sha3_256_hash = hashlib.sha3_256(raw_password.encode()).hexdigest()
        blake2b_hash = hashlib.blake2b(raw_password.encode()).hexdigest()

        return {
            'MD5': md5_hash,
            'SHA1': sha1_hash,
            'SHA3-256': sha3_256_hash,
            'BLAKE2b': blake2b_hash,
        }

# Entry point of the program
if __name__ == "__main__":
    main()
