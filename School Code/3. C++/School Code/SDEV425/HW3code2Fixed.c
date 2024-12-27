/*
   Modified by Brian Walters
   Date: 25 July 2024
   Class : SDEV 425 / Spring 2024
   Professor : Justin Boswell
   Homework 3
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Function prototypes
void fillPassword(size_t, char[]);
void showResults(char);
void showMenu(void);
bool isValidInput(char);
void clearInputBuffer(void);

// Define a variable to hold a password
// and the copy
char password[15];
char cpassword[15];

int main(void)
{
    // Welcome the User
    printf("Welcome to the C Array Program!\n");

    // Variables
    char cont[3] = "y"; // To continue with loop, use an array to hold the input string
    int cVar = 0;       // process variable

    // Main loop
    bool running = true;
    while (running)
    {
        // Display menu and Get Selection
        while (cont[0] != 'E' && cont[0] != 'e')
        {
            // Display the Menu
            showMenu();

            // Get the user selection
            char selection;
            if (scanf(" %c", &selection) == 1)
            {
                // Clear buffer
                clearInputBuffer();

                // Validate input
                if (isValidInput(selection))
                {
                    // Display the menu response
                    showResults(selection);
                    cont[0] = selection;
                }
                else
                {
                    printf("Invalid input. Please enter a valid selection.\n");
                }
            }
        }

        // Call the Copy routine
        fillPassword(sizeof(password), password);

        // Display variable values
        printf("password is %s\n", password);
        printf("cVar is %d\n", cVar);

        // Copy password   ******* If saving the password, other security precations should be observed such as hashing and more.
        memcpy(cpassword, password, sizeof(password));

        // Pause before exiting
        printf("Press Enter to confirm your exit, or any other key to return to the menu.\n");
        char confirm = getchar();
        if (confirm == '\n')
        {
            running = false; // Exit the program
        }
        else
        {
            cont[0] = ' ';      // Reset cont to avoid exiting the menu loop
            clearInputBuffer(); // Clear the buffer to avoid any leftover input
        }
    }

    return 0;
}

// Make a String of '1's
void fillPassword(size_t n, char dest[])
{
    // Corrected loop to handle null terminator
    for (size_t j = 0; j < n - 1; j++)
    {
        dest[j] = '1';
    }
    // Add null terminator for string
    dest[n - 1] = '\0';
}

/* Display the Results*/
void showResults(char value)
{
    switch (value)
    {
    case 'F':
    case 'f':
        printf("Welcome to the Football season!\n");
        break; // Added missing break statement
    case 'S':
    case 's':
        printf("Welcome to the Soccer season!\n");
        break;
    case 'B':
    case 'b':
        printf("Welcome to the Baseball season!\n");
        break;
    case 'E':
    case 'e':
        printf("Exiting the Menu system!\n");
        break;
    default:
        printf("Please enter a valid selection\n");
    }
}

/* Display the Menu*/
void showMenu(void)
{
    printf("Enter a selection from the following menu.\n");
    printf("B. Baseball season.\n");
    printf("F. Football season.\n");
    printf("S. Soccer season.\n");
    printf("E. Exit the system.\n");
}

/* Validate the input */
bool isValidInput(char input)
{
    switch (input)
    {
    case 'F':
    case 'f':
    case 'S':
    case 's':
    case 'B':
    case 'b':
    case 'E':
    case 'e':
        return true;
    default:
        return false;
    }
}

/* Clear the input buffer */
void clearInputBuffer(void)
{
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF)
        ;
}