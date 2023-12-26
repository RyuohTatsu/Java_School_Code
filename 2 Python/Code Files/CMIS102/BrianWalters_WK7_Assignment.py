# Python code
# This program will collect and display  trip costs.
# Developer: Brian Walters CMIS102/7384
# Developed: April 26, 2023

# Main ---------------------------------------------------------------
def main():
    # Display Header
    Header()

    # Display Welcome message
    Welcome()

    # Call Functions
    # Initialize Variables.
    numPeep = 0
    numDay = 0
    # Initialize list.
    food = []
    gas = []
    
    # Get Inputs
    gas, food, numPeep, numDay, currency = Inputs(food, gas, numPeep, numDay)

    # Calculate
    totGas, totFood, totTrip, costPp = Calculate(gas, food, numPeep, numDay)

    #Display output
    Output(currency, numPeep, numDay, totGas, totFood, totTrip, costPp)

# Functions -----------------------------------------------------------------------------------------

# Header
def Header():
    print('Name: Brian Walters')
    print('Week 7 Assignment: Trip Cost Analysis.')
    print('CMIS 102/7384')
    
# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print('\nWelcome to B\'s trip cost analizer.')
   print('You will be prompted for number of people that went on the trip and the number of days the trip lasted.')
   print('Next you will input food and gas cost for each day of the tip.')
   print('You will see an output of the total cost of the trip, a breakdown for food and gas, and also each persons share of the cost.')
  
# Ask Input Questions -----------------------------
def Inputs(food, gas, numPeep, numDay):
    # Ask for number of People attending the trip.
    numPeep = int(input('\nPlease input the number of people that went on the trip.\n'))
    # Ask for the number of days the tip was.
    numDay = int(input('How many days did the trip last?\n'))
    # What currency was the tip in?
    currency = input('Please enter the currency that was used during your trip.\n')

    # Initialize loop to ask for cost inputs.
    r = numDay
    d = 1
    print('\nPlease input the cost for food and gas for each day.')
    while r > 0:
        gas.append(float(input(f'Cost of gas for day {d}.\n')))
        food.append(float(input(f'Cost of food for day {d}.\n')))
        d = d + 1
        r = r - 1
    return (gas, food, numPeep, numDay, currency)

# Calculate Function ----------------------------
def Calculate(gas, food, numPeep, numDay):
    # Initialize Variables.
    totGas = 0
    totFood = 0
    totTrip = 0
    costPp = 0
    i = 0

    # Loop to calculate list totals.
    while i < numDay:
        # Calculate cost for total gas.
        totGas = totGas + gas[i]

        # Calculate cost for total food.
        totFood = totFood + food[i]

        i = i + 1

    # Calculate cost for total trip.
    totTrip = totGas + totFood

    # Calculate cost for total trip per person.
    costPp = totTrip / numPeep

    return (totGas, totFood, totTrip, costPp)
    
# Output
def Output(currency, numPeep, numDay, totGas, totFood, totTrip, costPp):
    # Displays the calculated costs for the trip.
    print(f'\nYou went on a trip for {numDay} days with {numPeep} people and the currency was the {currency}.')
    print('{:<40}\t{:>10}'.format('Description of Cost                                  ','Totals'))
    print('{:<40}\t{:>10}'.format('__________________________________________','____________________'))
    print('{:<40}\t{:10.2f}'.format('Your total cost of gas for the trip was:\t', totGas))
    print('{:<40}\t{:10.2f}'.format('Your total cost of food for the trip was:\t', totFood))
    print('{:<40}\t{:10.2f}'.format('Your total cost of the trip was:          \t', totTrip))
    print('{:<40}\t{:10.2f}'.format('The cost per person for the entire trip was:\t', costPp))
    print('********* Thank you for using the trip cost calculator. ************')
          
#--- Execute -----------------------------------------------
main()
