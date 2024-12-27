//

#define __STDC_WANT_LIB_EXT1__
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <iostream>
#include <ctime>
#include <stddef.h>
#include <syslog.h>

using namespace std;

// Function prototypes
void fillPassword(size_t , char[]);
void showResults(char);
// should have void listed
void showMenu(void);
//the null-termination character
void copy(size_t, char[], char[]);

// Define a variable to hold a password
// and the copy
char password[15];
char cpassword[15];
char user[15];
char secret[15];
char shared[15];
int g=0;


int main(void)
{
    // NEW NEW NEW ... this is used to compare the user inputed password with a shared secret we already know about, this time it is in a text file not database
    /* Reading the SharedSecrets File
     populating the secret variable with the file */
    std::ifstream getFile; //must use std:: with the current libraries loaded
    getFile.open("Desktop:\\homework3\\sharedsecrets.txt");  //please make sure you have created this path or modify this line for your settings
    if (getFile.fail()){
    }
    /* with more time we would put error checking around this character limit to ensure attacker were not injecting malicious values */
    char secret[15];  
    getFile >> secret;
    while (!getFile.eof()){
        /*there is a single shared secret password in the sharedsecrets.txt file, we can read this directory into the variable*/
        getFile >> secret;
    }
   
    // NEW NEW NEW ... this allows us to prompt the user to see if they know the shared secret, the username is not used, but will help in our audit logs
    // If the SharedSecret it correct
    // So much more work could be done here, by masking the password input,
    //however,the needed libraries have been deprecated and I am working on alternatives
    printf("Please enter your username\n");
    scanf("%s", user);  // reading the username into a variable for audit logging
    printf("Please enter the shared secret\n");
    /*reading the shared secret into a variable, I would like to mask this but for now it works to authorize access to the menu */
    scanf("%s", shared);
    
    //this clears the screen and compares the secret in the textfile with the entry from the user
    std::cout << "\033[2J\033[1;1H";
    /* this is uncommented so you can see in the terminal the value of secret read from the text file*/
    printf("%s", secret);
    // this is uncommented so you can see the input from the user
    printf("%s", shared);
    // if the user knows the current secret they will be allowed to the menu system
    if (strcmp(secret,shared)==0){
        
        // Welcome the User
         printf("Welcome to the C Array Program!\n");
        
        // Variables
        char cont = 'y'; // To continue with loop
        int cVar = 0; // process variable
        
        // Display menu and Get Selection
        while (cont != 'E' && cont != 'e') {
            /* Display the Menu */
           showMenu();
           //Get the user selection
              cont = getchar();
        }
        // Call the Copy routine
        fillPassword(sizeof(password),password);
        
        // Display variable values
        printf("password is %s\n", password);
        printf("cVar is %d\n", cVar);
        
        
        // Copy password
        memcpy(cpassword, password,sizeof(password));
    
        // Pause before exiting
        char confirm;
        printf("Confirm your exit!");
        confirm = getchar();
        return 0;
        
    }else
    {
        // NEW NEW NEW ... lots of new lines to provide auditing around the user of the menu system
        time_t now = time(0);  // grabs the system time
        // convert the time to a string that can be printed
        char* stamp = ctime(&now);
        /* clears the screen without having to use system (), this is a safeguard against attackers*/
        std::cout << "\033[2J\033[1;1H";
        printf("You have entered the wrong secret, the program will not termination\n");
        printf("This event has been logged\n");
        // opens the file on our system to write an audit event
        std::ofstream getAudit;
        // if you want a different directory change this line
        getAudit.open("Desktop:\\homework3\\auditlog.txt", ios::in | ios::out | ios::app);
        // checks to see if the text file is accessible
        if (!getAudit.is_open()){
            /* it is important to modify the string in the path to meeting your settings*/
            printf ("Audit log failure");
        }else{
            /* written to the terminal, just for us, we would not want to let the users know of a filed or successful audit entry*/
            printf ("Audit entry successful");
            getAudit << stamp  <<" " <<user <<" " <<shared << "\n";
            // writes the audit event to the text file
            getAudit.close();
        }
    }

    }
// Make a String of '1's
void fillPassword(size_t n, char dest[]) {
    // Should be n-1
    for (size_t j = 0; j < n - 1; j++) {
        dest[j] = '1';
    }
    // Add null terminator for string
    dest[n] = '\0';
}

/* Display the Results*/
void showResults(char value) {
    switch (value){
        case 'F':
        case 'f':
            // clears the terminal screen
            std::cout << "\033[2J\033[1;1H";
            printf("Welcome to the Football season!\n");
            // waits for the user input
            std::cin.get();                   
            break;
        case 'S':
        case 's':
            // Each case requires updating
            std::cout << "\033[2J\033[1;1H";
            printf("Welcome to the Soccer season!\n");
            std::cin.get();
            break;
        case 'B':
        case 'b':
            std::cout << "\033[2J\033[1;1H";
            printf("Welcome to the Baseball season!\n");
            std::cin.get();
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
void showMenu(void) {
    printf("Enter a selection from the following menu.\n");
    printf("B. Baseball season.\n");
    printf("F. Football season.\n");
    printf("S. Soccer season.\n");
    printf("E. Exit the system.\n");
}

M