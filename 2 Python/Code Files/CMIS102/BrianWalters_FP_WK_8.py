# Python code
# This program will calculate house cleaning with different types of cleaning services.
# Developer: Brian Walters CMIS102/7384
# Date: March 28, 2023
# Modified: April 8, 2023
    # Added a deep cleaning service.
    # Created functions for each bit of information.
    # Added for loops on Rooms and Bath functions.
    # Added while True loops to the yes and no questions.
# Modified: May 5, 2023
    # Added a senior discount.
    # Created lists for name, age, address, and store sales gathering information.
    # Added function and loops for lawn care services.
    # Added while loop to main to gather customer info and ask which service is being requested.
    # Added function to calculate store totals.
    # Formatted output to look more professional.
    
# Funtions -----------------------------

# Header -------------------------------
def Header():
    print('Name: Brian Walters')
    print('Week 8 Finial Project: House Cleaning and Lawn Service program.')
    print('CMIS 102/7384 \nDate: 5/5/2023')

# Welcome ------------------------------
def Welcome():
    #Display welcome message including initial price of cleaning Living, Dinning, and Kitchen areas.
    #Basic cleaning involves dusting, laundry, dishes, vacuum, and basic straitening.
    print("\nWelcome to B's Cleaning and Lawn Service.")
    print('Our basic cleaning package cost $115 and includes: \
Dusting, Laundry, Dishes, Vacuuming, and basic straightening of the Living, Kitchen,\
and Dinning areas. Please look through our optional services and select witch ones \
you would like to include and we will provide you with a total quote and price breakdown.')
    # Lawn Care ------------- BDW May 5, 2023
    print('We are pround to introduce our lawn care packages which include mowing, edging, and pruning your bushes.')
    print('If interested please select the lawn care program to choose you needs.')
    # Senior Discount  ------------- BDW May 5, 2023
    print('We now offer a Senior Discount. 10% for anyone over the age of 50.')
    print('Please ask for assistance if you have any questions.')

# Get Name ------------------------------ ------------- BDW May 5, 2023
def GetName(): 
    validName = False

    # Prompt for customer name
    name = input('\nPlease enter your name or hit <Ent> to exit:\t')

    # Replace spaces with null
    name1 = name.replace(" ","")

    # Check for alpha only
    if (name1.isalpha()):
        # Convert user input "name" to Upper case
        name = name.upper()
        validName = True

    return (name, validName)

# Get Age and Address ------------------------------ ------------- BDW May 5, 2023
def AgeAddress():

    # Prompt for customer age.
    while True:
        try:
            age = int(input('\nPlease enter you age:\t'))
        except ValueError:
            print("Invalid value. Please enter an integer! Let's try again...")
        else:
            break

    # Prompt for customer name
    address = input('\nPlease enter your Address:\t')
    address = address.upper()

    return (age, address)

# Get Rooms -----------------------------
def Rooms():
    #Prompt the user for number of bedrooms rooms.
    for numRm in range(1, 6):
        numRm = int(input('\nEnter Number of rooms you would like cleaned. \t'))
        if numRm == 1 or numRm == 2 or numRm == 3 or numRm == 4 or numRm == 5:
            print(f'You want {numRm} cleaned.')
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
            print(f'You want {numBath} cleaned.')
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

# Cleaning Calculations ---------------------------------
def CleanCalculations(numRm, numBath, totWin, totFl, dpCln):
    # Initialize variables
    perRm = 40 # Per room
    LDK = 115 #L iving, Dinning, Kitchen Initial cost
    bath = 55 # bathrooms
    
    # Calculate cost of rooms
    totRm = numRm * perRm
    # Calculate cost of Bathrooms
    totBath = numBath * bath
    # Calculate cost of Windows
    totWin
    # Calculate cost of total Floors
    totFl
    # calculate cost of deep clean
    dpCln
    # Calculate the final cost of purchase (sum of total cost)
    totCost = dpCln + totFl + totWin + totBath + totRm + LDK
    return (totCost, totRm, totBath, totWin, totFl, dpCln, LDK)

# Senior Discount--------------------------- BDW May 5, 2023
def SenCal(totCost, age): 
    senDis = 0
    if age > 49:
        senDis = (totCost * .10)
    return (senDis)

# Display Cleaning Cost --------------------------------- BDW May 5, 2023 ------formatted
def CleanCost(totRm, totBath, totWin, totFl, dpCln, totCost, LDK, senDis):    
    #Display the results (totalCost and priceList)
    print('{:<40}\t{:<10}'.format('Fee Name','Cost'))
    print('{:<40}\t{:<10}'.format('________________________________________','__________'))
    print('{:<40}\t{:10.2f}'.format('Basic Cleaning Fee:', LDK))
    print('{:<40}\t{:10.2f}'.format('Total Rooms fee:', totRm))
    print('{:<40}\t{:10.2f}'.format('Bathroom cleaning fee:', totBath))
    print('{:<40}\t{:10.2f}'.format('Window cleaning fee:', totWin))
    print('{:<40}\t{:10.2f}'.format('Floor cleaning fee:', totFl))
    print('{:<40}\t{:10.2f}'.format('Deep cleaning service fee:', dpCln))
    print('{:<40}\t{:10.2f}'.format('Senior Discount Applied:', senDis))
    print('{:<40}\t{:10.2f}'.format('Total Cost:', (totCost - senDis)))

# Get Lawn Size ----------------------------- BDW May 5, 2023
def Size():
    Invalid = True
    
    # Validate input 
    while (Invalid):
        # Prompt the user for the size of the yard in Square Feet
        sqFt = int(input('\nEnter your yard size in Square Feet. \t'))

        # Display error msg
        if (sqFt < 0):
            print('I am sorry but that is an invalid input. Please try again.')
        elif (sqFt > 87120):
            print('Sorry to say that we are too understaffed to handle a yard \
your size. May I refer you to a larger lawn service that may be able to help?')
            quit()
        else:
            print(f'You have {sqFt} square feet to be mowed.')
            Invalid = False
    return (sqFt)

# Get Edge Size ----------------------------- BDW May 5, 2023
def Edging():
    Invalid = True
    
    # Validate input 
    while (Invalid):
        # Prompt the user for the size of the yard in Square Feet
        linFt = int(input('\nEnter the amount of feet you require to be edged. \t'))

        # Display error msg
        if (linFt < 0):
            print('I am sorry but that is an invalid input. Please try again.')
        elif (linFt > 1680):
            print('Sorry to say that we are too understaffed to handle a yard \
your size. May I refer you to a larger lawn service that may be able to help?')
            quit()
        else:
            print(f'You have {linFt} linear feet to be edged.')
            Invalid = False
    return (linFt)

# Get Number of Shrubs ----------------------------- BDW May 5, 2023
def Shrub():
    Invalid = True
    
    # Validate input 
    while (Invalid):
        # Prompt the user for the size of the yard in Square Feet
        numShrub = int(input('\nEnter the number of shrubs you would like pruned. \t'))

        # Display error msg
        if (numShrub < 0):
            print('I am sorry but that is an invalid input. Please try again.')
        elif (numShrub > 20):
            print('Sorry to say that we are too understaffed to handle a yard \
your size. May I refer you to a larger lawn service that may be able to help?')
            quit()
        else:
            print(f'You have {numShrub} to be pruned.')
            Invalid = False
    return (numShrub)

# Lawn Calculations ---------------------------------- BDW May 5, 2023
def LawnCalculations(sqFt, linFt, numShrub):
    # Initialize variables
    persqFt = .02 
    perlinFt = .70 
    perShrub = 20 
    
    # Calculate cost of Lawn
    totLawn = sqFt * persqFt
    # Calculate cost of Edging
    totEdge = linFt * perlinFt
    # Calculate cost of Shrubs
    totShrub = numShrub * perShrub

    #Calculate the final cost of lawn (sum of total cost)
    totCost = totLawn + totEdge + totShrub
    return (totCost, totLawn, totEdge, totShrub)

# Display Lawn Cost ---------------------------------- BDW May 5, 2023
def LawnCost(totCost, totLawn, totEdge, totShrub, senDis):    
    #Display the results (totalCost and priceList)
    print('{:<40}\t{:<10}'.format('Fee Name','Cost'))
    print('{:<40}\t{:<10}'.format('________________________________________','__________'))
    print('{:<40}\t{:10.2f}'.format('Lawn Fee is:', totLawn))
    print('{:<40}\t{:10.2f}'.format('Edging Fee is:', totEdge))
    print('{:<40}\t{:10.2f}'.format('Shrub Pruning Fee is:', totShrub))
    print('{:<40}\t{:10.2f}'.format('Senior Discount Applied:', senDis))
    print('{:<40}\t{:10.2f}'.format('Total Cost:', (totCost - senDis)))

# Store Output ------------------------------------- BDW May 5, 2023
def DisplaySalesTotals (custNames, custAddress, custAges, custSales, clnORlwn, seniorDis):
    # This function first displays all the customer info and store totals.
    totSenior = 0
    totalSales = 0
    
    lenCust = len(custNames)
    print('{:<20}\t{:<3}\t{:<20}\t{:<10}\t{:<10}\t{:<10}'.format('Name','Age','Address','Service','Senior', 'Total Cost'))
    print('{:<20}\t{:<3}\t{:<20}\t{:<10}\t{:<10}\t{:<10}'.format('____________________','___','____________________','__________','__________','__________'))
    i = 0
    dis = 0
    while (i < lenCust):
        print('{:<20}\t{:<3d}\t{:<20}\t{:10}\t{:10.2f}\t{:10.2f}'.format(custNames[i], custAges[i], custAddress[i], clnORlwn[i], seniorDis[i], custSales[i]))
        totalSales = totalSales + custSales[i]
        totSenior = totSenior + seniorDis[i]
        i = i + 1

    print('{:<20}\t{:<3}\t{:<20}\t{:<10}\t{:<10}\t{:<10}'.format('____________________','___','____________________','__________','__________','__________'))
    print('{:<20}\t{:<3}\t{:<20}\t{:<10}\t{:<10.2f}\t{:<10.2f}'.format('Totals','','', '', totSenior, totalSales))


# Main -------------------------------------------
def main():
    #Initialize variables
    moreCustomers = True
    Service = None
    
    # Initialize Lists ------------- BDW May 5, 2023
    custNames = []
    custAddress = []
    custAges = []
    custSales = []
    clnORlwn = []
    seniorDis = []
    
    # Display header
    Header()
    
    # Display Welcome message
    Welcome()

    # Validate input loop -------------- BDW May 5, 2023
    while (moreCustomers):
        
        # Prompt user for customer name -------------- BDW May 5, 2023
        custName, validName = GetName()
        moreCustomers = validName
        
        if (validName):

            Invalid = True

            # Prompt user for age and address-------------- BDW May 5, 2023
            age, address = AgeAddress()
    
            # Validate input loop -------------- BDW May 5, 2023
            while (Invalid):
                # Prompt For Cleaning or Lawn Services -------------- BDW May 5, 2023
                Service = input('\nPlease choose what service you would like. Type: Lawn or Cleaning.\t')
                Service = Service.upper()

                # Cleaning Service
                if Service == 'CLEANING':
                    print('\nYou would like the cleaning service. Please fill out the questionnaire for an estimate.')
                    print('At this time we are unable to handle large houses with over 6 rooms or 6 bathrooms.')
                    # Cleaning Functions
                    numRm = Rooms()

                    numBath = Bath()

                    totWin = Window()

                    totFl = Floor()

                    dpCln = Deep()

                    # Calculate costs
                    totCost, totRm, totBath, totWin, totFl, dpCln, LDK = CleanCalculations(numRm, numBath, totWin, totFl, dpCln)
                    senDis = SenCal(totCost, age)

                    # Display output
                    CleanCost(totRm, totBath, totWin, totFl, dpCln, totCost, LDK, senDis)
                    Invalid = False

                # Lawn Service    
                elif Service == 'LAWN':
                    print('\nYou would like the cleaning service. Please fill out the questionnaire for an estimate.')
                    print('At this time we do not handle lawns over  sq. feet (2 acres), edging over 1680 linear feet, and over 20 Shrubs.')
                    print('Enter 0 if you do not require the service.')
                    # Lawn Service Functions -------------- BDW May 5, 2023
                    sqFt = Size()

                    linFt = Edging()

                    numShrub = Shrub()

                    # Calculate Costs
                    totCost, totLawn, totEdge, totShrub = LawnCalculations(sqFt, linFt, numShrub)
                    senDis = SenCal(totCost, age)

                    # Display Output
                    LawnCost(totCost, totLawn, totEdge, totShrub, senDis)
                    Invalid = False

                # Invalid Input
                else:
                    print('\n****************Invalid input. Please try again.************************')
                    
                    
            # Populate arrays
            custNames.append(custName)
            custAddress.append(address)
            custAges.append(age)
            custSales.append(totCost - senDis)
            clnORlwn.append(Service)
            seniorDis.append(senDis)


    # Display Sales Totals -------------- BDW May 5, 2023
    DisplaySalesTotals(custNames, custAddress, custAges, custSales, clnORlwn, seniorDis)

	
# Execute ------------------------------------------
main()
