# Python code
# This program will calculate and display the cost of purchasing a set of tires.
# The user will be prompted for how many tires to purchase. 
# The program will validate the user input.

# Developer: Faculty CMIS102   Date: Jan 31, 2014
# Modified: BLB	- modified for Validation	Jun 4, 2017	
# Modified: BLB	- modified for Functions	Jun 22, 2017	


# Define Functions -----------------------------------------------------------------------------------------

# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print("\nWelcome to Bernie's Tire service program")
   print("\nThis program will calculate the cost of your tire purchase , including installation")


# GetNumTires ------------------------
def GetNumTires ():
	# This function prompts for the number of tires and validates between 0 and 99
	# Input: none
	# Output: numTires

	numTires = -1
	
	#Prompt.Get user response user for number of tires
	numTires = int(input("\n\n How many tires would you like to purchase (1-99) ? "))

	# Validate input 
	if (numTires <= 0 or numTires > 99):
		# Display error msg
		print("\n Please enter a positive number (1-99): ")
		numTires = int(input("\n\n How many tires would you like to purchase (1-99) ? "))

	return(numTires)


# CalCustCost ------------------------
def CalCustCost (numTires):
	# This function calculates all costs per customer
	# Input:  numTires  - number of tires purchased
	# Output: tireCost, installCost, totalCost - total customer cost (tires + install)        


	tirePrice = 140.0	# Notice that I'm assigning these values to variables
	installPrice = 5	# These variables will be used in the calculations.

	#Calculate the cost of tires
	tireCost = tirePrice * numTires

	#Calculate the cost if installation
	installCost = installPrice * numTires

	#Calcuate the total cost 
	totalCost = tireCost + installCost

	return(tireCost,installCost,totalCost)


# DisplayOutput ------------------------
def DisplayCustOutput (numCTires, tireCCost,installCCost,totalCCost):
   # This function displays the number of tires purchased and the total cost
   # Input: numCTires  - number of tires purchased
   #        tireCCost - tire purchase cost        
   #        installCCost - install purchase cost        
   #        totalCCost - total purchase cost        
   # Output: none

   print("\n\n *** Thank you for your purchase !")
   print("\n *** The number of tires purchased:    ", numCTires)
   print("\n *** The cost of tires purchased:     $", tireCCost)
   print("\n *** The installation cost:           $", installCCost)
   print("\n *** The total cost of your purchase: $", totalCCost)


# Main ---------------------------------------------------------------
def main():
	# Display Welcome message
	Welcome()

	#Prompt user for number of tires 
	numTires = GetNumTires()

	#Calculate the customer cost
	tireCost,installCost,totalCost = CalCustCost (numTires)

	#Diplay output
	DisplayCustOutput (numTires, tireCost, installCost, totalCost)

#--- Execute -----------------------------------------------
main()
