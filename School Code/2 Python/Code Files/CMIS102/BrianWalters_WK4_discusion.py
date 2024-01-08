# Python code
# This program will calculate Braking distance.
# Developer: Brian Walters CMIS102/7384
# Date: April 7, 2023



 

# Define Functions -----------------------------------------------------------------------------------------

# Header
def Header():
    print('Name: Brian Walters')
    print('Week 3 Assignment: Calculate Breaking distance.')
    print('CMIS 102/7384 \nDate: 4/7/2023')
    
# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print('\nWelcome to the Breaking game calculator. You are going 200 Kilometers an hour and need to break to 70 Kilometers an hour in able to get around the corner.')
   print('\nYou will be prompted to enter your breaking distance and break pressure level to see if you can stop in time.')


# Get GetBrkDis ------------------------
def GetBrkDis():
   
    # This function prompts the user for which breaking marker they would like to break at.
	
    # Prompt.Get user response for Breaking Marker.
    brkDis = int(input('\nPick a breaking marker. 200 meters to 100 meters?\t'))
    if brkDis < 99 or brkDis > 201:
        print('If you are still alive try a number between 100 and 200.\t')
        brkDis = int(input('\nPick a breaking marker between 100 and 200 meters?\t'))
    return(brkDis)

# Get GetBrkPsi ------------------------
def GetBrkPsi():

    # This function prompts the user for how hard to push the breaks.
   
    #Prompt.Get user response break pressure.
    brkPsi = int(input('\nPick a breaking pressure between 70% and 95%?\t'))
    if brkPsi < 70 or brkPsi > 95:
        print('If you are still alive try a number between 70 and 95.\t')
        brkPsi = int(input('\nPick a breaking pressure between 70% and 95%?\t'))

    # This function calculates break pressure distance.
    return(brkPsi)


# CaltotDist ------------------------
def calTotDis(brkDis , brkPsi):

    # Initiate Variables

    slow = 200
    med = 150
    hard = 100   
    
    # Conversion
    if brkPsi < 78:
        bP = slow
    elif brkPsi >86:
        bP = hard
    else:
        bP = med
    
    # This function calculates total distance.
    totDis = brkDis - bP

    return(totDis)


# DisplayOutput ------------------------
def DisplayOutput(totDis):
    
    # This function prints if you made the corner or not.

    print("\n\nLet's see if you made it!")
    if totDis == 0:
        print('\nCongrats! You made the turn!')
    elif totDis >= 1:
        print('\nYou made the turn but lost time.')
    elif totDis <= -1:
        print('\nYou are dead!')
    print('\nYour total distance was:', int(totDis),'meters')


# Main ---------------------------------------------------------------
def main():
    # Display Welcome message
    Welcome()

    # Call Functions
    brkDis = GetBrkDis()

    bP = GetBrkPsi()

    totDis = calTotDis(brkDis , bP)

    #Display output
    DisplayOutput(totDis)

#--- Execute -----------------------------------------------
main()
