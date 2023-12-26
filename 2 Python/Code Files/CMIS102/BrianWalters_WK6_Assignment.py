# Python code
# This program will determine if a password meets the critera assigned.
# Developer: Brian Walters CMIS102/7384
# Developed: April 22, 2023
 
# Main ---------------------------------------------------------------
def main():
    # Display Header
    Header()

    # Display Welcome message
    Welcome()
    
    # Initialize Loop
    length = 20 # Loop control
    spaces = 20
    alNum = 20
    chk = True
    while chk:
    
        # Prompt User for Password
        password = input('\nEnter your password:\t')

        # Call Functions
    
        # Check Length
        Valid = Length(password)
        if Valid == False:
            length = 1

        # Check for spaces
        if length == 1:
            Valid = Space(password)
            if Valid == False:
                spaces = 1
            else:
                length = 20 # Loop control
                spaces = 20
                alNum = 20 
        
        # Check for letter and number
        if spaces == 1:
            Valid = AlphaNum(password)
            if Valid == False:
                alNum = 1
            else:
                length = 20 # Loop control
                spaces = 20
                alNum = 20

        if alNum == 1:
            chk = False
            
    #Display output
    Output()

# Functions -----------------------------------------------------------------------------------------

# Header
def Header():
    print('Name: Brian Walters')
    print('Week 6 Assignment: Password verifier.')
    print('CMIS 102/7384')
    
# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print('\nWelcome to B\'s password verifier.')
   print('Input a password between 8 and 20 characters long. No spaces allowed. Password must contain at least one number and one letter.')
   print('This program will let you know if your password meets the criteria.')
  
# Check Length -----------------------------
def Length(password):
    # This function will check if the password is within the character limits.
    if (len(password) < 8):
        Valid = True
        print('Password does not contain enough characters.')
    elif (len(password) > 20):
        Valid = True
        print('Password contains to many characters.')
    else:
        Valid = False
    return (Valid)    

# Check for spaces ----------------------------
def Space(password):
    # This function will ensure no 'spaces' are present.
    if (" " in password):
        Valid = True
        print('Your password is invalid because it contains spaces.')
    else:
        Valid = False
    return (Valid)
            
# Check for letter and number -------------------------------
def AlphaNum(password):
    # This function will check if the password has at least one letter and one number present.
    # Initializing variable
    alp = 1
    dig = 1
    Valid = True
 
    # For Loop
    for alpNum in password:
        if alpNum.isalpha():
            alp = 2
        if alpNum.isdigit():
            dig = 2
        if (alp + dig == 4):
            Valid = False
    if alp == 1:
        print('Your password is invalid because it does not contain a letter.')
    if dig == 1:
        print('Your password is invalid because it does not contain a number.')
    return (Valid)

# Output
def Output():
    # Displays the result of the checks.
    print(f'\nCongrats, your password is accepted.')
          
#--- Execute -----------------------------------------------
main()
