# Python code
# This program will calculate distance ran for the week.
# Developer: Brian Walters CMIS102/7384
# Developed: April 12, 2023
 

# Define Functions -----------------------------------------------------------------------------------------

# Header
def Header():
    print('Name: Brian Walters')
    print('Week 5 Discussion: Calculate distance ran for the week.')
    print('CMIS 102/7384')
    
# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print('\nWelcome to the miles ran in a week compiler.')
   print('\nYou will be prompted to enter your miles ran for each day.')


# Get Miles ------------------------
def Miles():
    # This function will get miles per day for one week.
    dayMiles = 0
    totMiles = 0
    d = 1
    while d < 7:
        Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for Day in Days:
            print('\nEnter Miles ran for',Day,'.')
            dayMiles = int(input())
            if dayMiles < 0:
                print('You cannot run negative miles.')
                print('\nEnter Miles ran for',Day,'.')
                dayMiles = int(input())
            totMiles += dayMiles
        print('Finished input.')
        d = d + 8
    else:
        False
    return (totMiles)

            
# Get Miles ------------------------

def Result(totMiles):
    # This fuction displays the result.
    print('\nThe total number of miles you ran for the week is:', totMiles)


# Main ---------------------------------------------------------------
def main():
    # Display Header
    Header()

    # Display Welcome message
    Welcome()

    # Call Functions
    totMiles = Miles()

    #Display output
    Result(totMiles)

#--- Execute -----------------------------------------------
main()
