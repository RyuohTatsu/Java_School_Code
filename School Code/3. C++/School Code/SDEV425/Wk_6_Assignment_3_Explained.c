#include <stdio.h>
#include <string.h>

// Function prototypes
void fillPassword(size_t, char[]);
void showResults(char);
void showMenu(void);

// Define a variable to hold a password
char password[15];
char cpassword[15];

int main(void) {
    // Welcome the User
    printf("Welcome to the C Array Program!\n");

    // Variables
    char cont = 'y'; // To continue with loop
    int cVar = 0; // process variable

    // Display menu and Get Selection
    while (cont != 'E' && cont != 'e') {
        // Display the Menu
        showMenu();

        // Get the user selection
        cont = getchar();

        // Clear the input buffer to avoid issues with subsequent inputs
        while (getchar() != '\n');

        // Display the menu response
        showResults(cont);
    }

    // Call the Copy routine    
    fillPassword(sizeof(password) - 1, password); 

    // Display variable values
    printf("password is %s\n", password);
    printf("cVar is %d\n", cVar);

    // Copy password 
    memcpy(cpassword, password, sizeof(password));

    // Pause before exiting
    char confirm;
    printf("Confirm your exit! Press Enter to exit.");
    confirm = getchar(); 
    return 0;
}

// Make a String of '1's
void fillPassword(size_t n, char dest[]) {
    for (size_t j = 0; j < n; j++) {
        dest[j] = '1';
    }
    // Add null terminator for string
    dest[n] = '\0';
}

/* Display the Results */
void showResults(char value) {
    switch (value) {
        case 'F':
        case 'f':
            printf("Welcome to the Football season!\n");
            break;
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

/* Display the Menu */
void showMenu(void) {
    printf("Enter a selection from the following menu.\n");
    printf("B. Baseball season.\n");
    printf("F. Football season.\n");
    printf("S. Soccer season.\n");
    printf("E. Exit the system.\n");
}
/*
##STR31-C: Guarantee that storage for strings has sufficient space for character data and the null terminator.
##The fillPassword function now properly ensures that the array has enough space by using n-1 to fill characters and then adding a null terminator explicitly.

##MSC24-C: Do not use deprecated or obsolescent functions.
##There were no deprecated or obsolescent functions in the original code that needed to be replaced.

##FIO34-C: Distinguish between characters read from a file and EOF or WEOF.
##Not applicable here as there is no file reading in the provided code.

##MSC17-C: Finish every set of statements associated with a case label with a break statement.
##Added missing break statement in the showResults function for the 'F' and 'f' cases.

##MSC33-C: Do not pass invalid data to the asctime() function.
##Not applicable here as there is no usage of asctime() in the provided code.

##DCL20-C: Explicitly specify void when a function accepts no arguments.
##The showMenu function prototype and definition now explicitly specify void.

##MEM30-C: Do not access freed memory.
##Not applicable here as there was no dynamic memory allocation and freeing in the provided code.
*/