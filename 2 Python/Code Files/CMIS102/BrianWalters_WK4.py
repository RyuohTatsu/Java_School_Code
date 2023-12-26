# Python code
# This program will calculate house cleaning with different types of cleaning services.
# Developer: Brian Walters CMIS102/7384
# Date: March 282, 2023

print('Name:   Brian Walters')
print('Week 3 Assignment')
print('CMIS 102/7384  3/28/2023')

def main():
    
#Initialize variables 
    perRm = 40 #Per room
    LDK = 115 #Living, Dinning, Kitchen Initial cost
    bath = 55 #bathrooms
    winPrm = 22 #Windows per room
    winLDK = 45 #Windows for LDK
    cptPrm = 25 #Carpet Floors ldk
    cptLDK = 50 #Carpet Floors ldk
    wdLDK = 30 #Wood floors ldk
    wdPrm = 15 #Wood floors per room
    yes = ['yes', 'y', 'Y', 'Yes']
    no = ['No', 'No', 'n', 'N']
    wood = ['wood', 'Wood']
    carpet = ['carpet', 'Carpet']
    WD = wood
    CPT = carpet

#Display welcome message including initial price of cleaning Living, Dinning, and Kitchen areas.
#Basic cleaning involves dusting, laundry, dishes, vacuum, and basic straitening.
    print('Welcome to Sanford Cleaning Service. Our basic cleaning package includes:\
Dusting, Laundry, Dishes, Vacuuming, and basic straightening of the Living, Kitchen,\
and Dinning areas. Please look through our optional services and select witch ones\
you would like to include and we will provide you with a total quote and price breakdown.')
    print('\nPlease ask for assistance if you have any questions.')

#Prompt the user for number of bathrooms. Price includes floors and windows in bathroom.
    numBath = int(input('\nPlease enter number of bathrooms you would like cleaned. Note:\
Price for the bathroom includes floor and window cleaning. \t'))
    if numBath < 1:
        totBath = numBath * 0
    else:
        totBath = numBath * bath

#Prompt the user if they want windows cleaned.
    winCln = input('\nWould you like to have your windows cleaned? yes or no \t')
    if 'yes':
        winL = input('Living, Kitchen, and Dinning area windows? yes or no \t')
        if winL == 'yes':
            costwinLDK = winLDK * numRm
        else:
            costwinLDK = winLDK * 0
        winRm = input('Room windows? yes or no \t')
        if winRm == 'yes':
            costwinPrm = winPrm * numRm
        else:
            costwinPrm = winPrm * 0
    else:
        totwin = 0

#Prompt the user if they want floors deep cleaned.
    flCln = input('\nWould you like to have your floors deep cleaned? yes or no \t')
    if 'yes':
        tyFl = input('Do you have wood or carpet? wood or carpet \t')

#Wood Floors                  
        if tyFl == 'wood':
            wdL = input('Living, Kitchen, and Dinning area floors? yes or no \t')
            if wdL == 'yes':
                costwdLDK = wdLDK * numRm
            elif tyFl != 'wood':
                wdCost = (wdPrm + wdLDK) * 0
            wdR = input('Room floors? yes or no \t')
            if wdR == 'yes':
                costwdPrm = wdPrm * numRm
            elif wdR != 'yes':
                wdCost = (wdPrm + wdLDK) * 0

#Carpets                            
        elif tyFl == 'carpet':
            cptL = input('Living, Kitchen, and Dinning area floors? yes or no \t')
            if cptL == 'yes':
                costcptLDK = cptLDK * numRm
            elif cptL != 'yes':
                cptCost = (carPrm + carLDK) * 0
            cptR = input('Room floors? yes or no \t')
            if cptR == 'yes':
                costcptPrm = cptPrm * numRm
            elif cptL != 'yes':
                cptCost = (carPrm + carLDK) * 0
        
    else:
        totFl = 0

#Prompt the user for number of bedrooms rooms.
    numRm = int(input('\nEnter Number of rooms you would like cleaned. \t'))
    if 1 <= numRm <= 4:
        totRm = numRm * perRm
    elif numRm > 5:
        print('Sorry to say that we are understaffed to handle a house\
your size. May I refer you to a larger cleaning service that may be able to help?')
    else:
        totRm = 0

#Calculate cost of Windows
    totWin = costwinLDK + costwinPrm
#Calculate cost of total Floors
    totFl = ((costcptLDK + costcptPrm) (costwdLDK + costwdPrm) + (cptCost + wdCost))
#Calculate the final cost of purchase (sum of total cost)
    totcost = totWin + totFL + totBath + totRm + LDK
#Display the results (totalCost and priceList)
    print('Basic living, Dinning, Kitchen area fee:\t', LDK)
    print('Bathroom cleaning fee:\t', totBath)
    print('Window cleaning fee:\t', totWin)
    print('Floor cleaning fee:\t', totFL)
    print('Total cleaning services will cost:\t', totCost)


# Execute -----------------------------
main()




