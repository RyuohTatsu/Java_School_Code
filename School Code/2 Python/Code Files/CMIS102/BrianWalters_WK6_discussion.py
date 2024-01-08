# Python code
# This program will analize some characteristics of a string.
# Developer: Brian Walters CMIS102/7384
# Developed: April 19, 2023
 

# Main ---------------------------------------------------------------
def main():
    # Display Header
    Header()

    # Display Welcome message
    Welcome()

    # Prompt User for Initals
    intials = input('\nEnter your intials:\t')

    # Prompt User for Favorite Movie Line
    favLine = input('\nEnter you favorite movie line.\n')

    # Call Functions
    
    # Make Lower
    favLineLow, lowInt = Lower(intials, favLine)

    #Check Initals
    cntInt = Intitials(favLineLow, lowInt)

    # Count Words
    wdCt = Words(favLineLow)

    # Make Title
    favLineCap, capInt = CapWords(favLineLow, lowInt)

    #Display output
    Output(favLineCap, capInt, wdCt, cntInt)

# Functions -----------------------------------------------------------------------------------------

# Header
def Header():
    print('Name: Brian Walters')
    print('Week 6 Discussion: Analize a string.')
    print('CMIS 102/7384')
    
# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print('\nWelcome to B\'s movie line analizer.')
   print('Input you initials and favorite movie line to see if they appear in the line.')
   print('This program will also tell you how many Words are in the line and capitalize every word.')
  
# Make Lower -----------------------------
def Lower(intials, favLine):
    # This function will make everything lowercase so it can check test cases.
    favLineLow = favLine.lower()
    lowInt = intials.lower()
    return (favLineLow, lowInt)    

# Make Title ----------------------------
def CapWords(favLineLow, lowInt):
    # This function will capitalize for presentation.
    favLineCap = favLineLow.title()
    capInt = lowInt.upper()
    return (favLineCap, capInt)
            
# Count Words -------------------------------
def Words(favLineLow):
    # This function will count the number of words.
    wdCt = favLineLow.strip(' ').count(' ')+1
    return (wdCt)
    
# Check Initals ---------------------------
def Intitials(favLineLow, lowInt):
    # This function will check if your initials appear in the movie line.
    cnt = favLineLow.strip(' ').count(lowInt)+1
    if cnt <= 1:
        cntInt = 0
    elif cnt >= 2:
        cntInt = cnt - 1
    return (cntInt)
    
# Output
def Output(favLineCap, capInt, wdCt, cntInt):
    # Displays results of the checks.
    print(f'\nYour intials {capInt} appeared {cntInt} times in your favorite movie line.')
    print(favLineCap)
    print(f'The are {wdCt} words in this movie line.')
          
#--- Execute -----------------------------------------------
main()
