# Python code
# This program will calculate house cleaning with different types of cleaning services.
# Developer: Brian Walters CMIS102/7384
# Date: March 28, 2023
# Modified: April 8, 2023
    # Added a deep cleaning service.
    # Created functions for each bit of information.
    # Added for loops on Rooms and Bath functions.
    # Added while True loops to the yes and no questions.

# Funtions -----------------------------

# Header -------------------------------
def Header():
    print('Name: Brian Walters')
    print('Week 3 Assignment: Calculate Breaking distance.')
    print('CMIS 102/7384 \nDate: 4/7/2023')

# Welcome ------------------------------
def Welcome():
    #Display welcome message including initial price of cleaning Living, Dinning, and Kitchen areas.
    #Basic cleaning involves dusting, laundry, dishes, vacuum, and basic straitening.
    print('\nWelcome to Sanford Cleaning Service.')
    print('Our basic cleaning package cost $115 and includes: \
Dusting, Laundry, Dishes, Vacuuming, and basic straightening of the Living, Kitchen,\
and Dinning areas. Please look through our optional services and select witch ones \
you would like to include and we will provide you with a total quote and price breakdown.')
    print('\nPlease ask for assistance if you have any questions.')

# Get Rooms -----------------------------
def Rooms():
    #Prompt the user for number of bedrooms rooms.
    for numRm in range(1, 6):
        numRm = int(input('\nEnter Number of rooms you would like cleaned. \t'))
        if numRm == 1 or numRm == 2 or numRm == 3 or numRm == 4 or numRm == 5:
            print('You want', numRm, 'cleaned.')
            break
        elif numRm < 1:
            print('I am sorry but that is an invalid input. Please try again.\t')
        else:
            print('Sorry to say that we are understaffed to handle a house \
your size. May I refer you to a larger cleaning service that may be able to help?')
            quit()
    return (numRm)

# Get Bathrooms --------------------------
def Bath():
    #Prompt the user for number of bathrooms. Price includes floors and windows in bathroom.

    for numBath in range(1, 6):
        numBath = int(input('\nPlease enter number of bathrooms you would like cleaned. Note: \
Price for the bathroom includes floor and window cleaning in the bathroom. \t'))
        if numBath == 1 or numBath == 2 or numBath == 3 or numBath == 4 or numBath == 5:
            print('You want', numBath, 'cleaned.')
            break
        elif numBath < 1:
            print('I am sorry but that is an invalid input. Please try again.\t')
        else:
            print('Sorry to say that we are understaffed to handle a house \
your size. May I refer you to a larger cleaning service that may be able to help?')
            quit()
    return (numBath)

# Ask about windows ------------------------
def Window():
    #Initialize variables
    yes_choices = ['yes', 'Yes', 'Y', 'y']
    no_choices = ['no', 'No', 'N', 'n']

    #Prompt the user if they want windows cleaned.
    while True:
        user_input = input('\nWould you like to have your windows cleaned? (yes or no) \t')
        if user_input in yes_choices:
            print('You want windows cleaned.')
            totWin = 62
            break
        elif user_input in no_choices:
            print('Windeow cleaning not requested')
            totWin = 0
            break
        else:
            print('Type yes or no')
    return (totWin)

# Ask about floors -------------------------                          
def Floor():
    #Initialize variables
    yes_choices = ['yes', 'Yes', 'Y', 'y']
    no_choices = ['no', 'No', 'N', 'n']
    
    #Prompt the user if they want floors deep cleaned.
    while True:
        user_input = input('\nWould you like to have your floors deeep cleaned? (yes or no) \t')
        if user_input in yes_choices:
            print('You want floors deep cleaned.')
            totFl = 75
            break
        elif user_input in no_choices:
            print('Floor cleaning not requested')
            totFl = 0
            break
        else:
            print('Type yes or no')
    return (totFl)

# Ask Deep Cleaning -------------------------                            
def Deep():       
    #Initialize variables
    yes_choices = ['yes', 'Yes', 'Y', 'y']
    no_choices = ['no', 'No', 'N', 'n']
    
    #Prompt the user if they want house deep cleaned.
    print('\n\nWe have an extra option of deep cleaning. This includes steam cleaning the \
furnature and also dishwasher, fridge and washer/dryer deep dives. This service cost an\
extra $250 and I promise that you will not be disapointed.')
    while True:
        user_input = input('\nWould you like to have your house deeep cleaned? (yes or no) \t')
        if user_input in yes_choices:
            print('You want deep cleaning.')
            dpCln = 250
            break
        elif user_input in no_choices:
            print('Floor cleaning not requested')
            dpCln = 0
            break
        else:
            print('Type yes or no')
    return (dpCln)

# Calculations ---------------------------------

def Calculations(numRm, numBath, totWin, totFl, dpCln):
    #Initialize variables
    perRm = 40 #Per room
    LDK = 115 #Living, Dinning, Kitchen Initial cost
    bath = 55 #bathrooms
    
    #Calculate cost of rooms
    totRm = numRm * perRm
    #Calculate cost of Bathrooms
    totBath = numBath * bath
    #Calculate cost of Windows
    totWin
    #Calculate cost of total Floors
    totFl
    #calculate cost of deep clean
    dpCln
    #Calculate the final cost of purchase (sum of total cost)
    totCost = dpCln + totFl + totWin + totBath + totRm + LDK
    return (totCost, totRm, totBath, totWin, totFl, dpCln, LDK)

# DisplayOutput ---------------------------------
def Cost(totRm1, totBath1, totWin1, totFl1, dpCln1, totCost1, LDK1):    
    #Display the results (totalCost and priceList)
    print('\nBasic living, Dinning, Kitchen area fee:\t$',LDK1)
    print('Total Rooms fee:\t$',totRm1)
    print('Bathroom cleaning fee:\t$',totBath1)
    print('Window cleaning fee:\t$',totWin1)
    print('Floor cleaning fee:\t$',totFl1)
    print('Deep cleaning service fee:\t$',dpCln1)
    print('Total cleaning services will cost:\t$',totCost1)

# Main -------------------------------------------
def main():
    # Display header
    Header()
    
    # Display Welcome message
    Welcome()

    # Call Functions
    numRm = Rooms()

    numBath = Bath()

    totWin = Window()

    totFl = Floor()

    dpCln = Deep()

    # Calculate costs
    totCost, totRm, totBath, totWin, totFl, dpCln, LDK = Calculations(numRm, numBath, totWin, totFl, dpCln)

    # Display output
    Cost(totRm, totBath, totWin, totFl, dpCln, totCost, LDK)

# Execute ------------------------------------------
main()
    

        
    
