# Python code
# This program will calculate house cleaning with different types of cleaning services.
# Developer: Brian Walters CMIS102/7384
# Date: March 282, 2023



def main():

    print('Name: Brian Walters')
    print('Week 3 Assignment: Calculate house cleaning with different types of cleaning services.')
    print('CMIS 102/7384 \nDate: 3/28/2023')
    
#Initialize variables 
    perRm = 40 #Per room
    LDK = 115 #Living, Dinning, Kitchen Initial cost
    bath = 55 #bathrooms
    windows = 62 #Window cleaning
    floors = 75 #Floor cleaning
    noWindows = 0 #Window cleaning
    noFloors = 0 #Floor cleaning
    yes_choices = ['yes', 'Yes', 'Y', 'y']
    no_choices = ['no', 'No', 'N', 'n']

#Display welcome message including initial price of cleaning Living, Dinning, and Kitchen areas.
#Basic cleaning involves dusting, laundry, dishes, vacuum, and basic straitening.
    print('\nWelcome to Sanford Cleaning Service.')
    print('Our basic cleaning package cost $115 and includes: \
Dusting, Laundry, Dishes, Vacuuming, and basic straightening of the Living, Kitchen,\
and Dinning areas. Please look through our optional services and select witch ones \
you would like to include and we will provide you with a total quote and price breakdown.')
    print('\nPlease ask for assistance if you have any questions.')

#Prompt the user for number of bedrooms rooms.
    numRm = int(input('\nEnter Number of rooms you would like cleaned. \t'))
    if 1 <= numRm <= 4:
        print('You want', numRm, 'cleaned.')
            
#Prompt the user for number of bathrooms. Price includes floors and windows in bathroom.
        numBath = int(input('\nPlease enter number of bathrooms you would like cleaned. Note: \
Price for the bathroom includes floor and window cleaning. \t'))
        if numBath >= 1:
            print('You have', numBath,'to be cleaned.')
    
#Prompt the user if they want windows cleaned.
        user_input = input('\nWould you like to have your windows cleaned? (yes or no) \t')
        if user_input in yes_choices:
            print('You want windows cleaned.')
            totWin = windows
        elif user_input in no_choices:
            print('Windeow cleaning not requested')
            totWin = noWindows
        else:
            print('Type yes or no')
                            
#Prompt the user if they want floors deep cleaned.
        user_input = input('\nWould you like to have your floors deeep cleaned? (yes or no) \t')
        if user_input in yes_choices:
            print('You want floors deep cleaned.')
            totFl = floors
        elif user_input in no_choices:
            print('Floor cleaning not requested')
            totFl = noFloors
        else:
            print('Type yes or no')
                    
#Calculate cost of rooms
        totRm = numRm * perRm
#Calculate cost of Bathrooms
        totBath = numBath * bath
#Calculate cost of Windows
        totWin
#Calculate cost of total Floors
        totFl
#Calculate the final cost of purchase (sum of total cost)
        totCost = totWin + totFl + totBath + totRm + LDK
#Display the results (totalCost and priceList)
        print('\nBasic living, Dinning, Kitchen area fee:\t', LDK)
        print('Total Rooms fee:\t', totRm)
        print('Bathroom cleaning fee:\t', totBath)
        print('Window cleaning fee:\t', totWin)
        print('Floor cleaning fee:\t', totFl)
        print('Total cleaning services will cost:\t', totCost)

    else:
        print('Sorry to say that we are understaffed to handle a house \
your size. May I refer you to a larger cleaning service that may be able to help?')

# Execute -----------------------------
main()




