# Python code
# This program will calculate weighted average grades for 4 students and display the highest.
# Developer: Brian Walters CMIS102/7384
# Developed: April 13, 2023
 

# Define Functions -----------------------------------------------------------------------------------------

# Header
def Header():
    print('Name: Brian Walters')
    print('Week 5 Assignment: Calculate weighted average grades for 4 students and display the highest.')
    print('CMIS 102/7384')
    
# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print('\nWelcome to the weighted average grade compiler.')
   print('\nYou will be prompted to enter your scores for each section. 0 - 110')
   print('\nThe student with the highest score will be displayed along with his score.')

# Get Grades ------------------------
def Grade(studentNames):    
    # This function will Prompt user for scores for each section and calculate average.
    # Variables
    disGrade = None
    qzGrade = None
    assGrade = None

    # Prompt for Grades
    while (disGrade == None):
        # Prompt user for discussion grade.
        print('\nInput discussion grade.')
        discussionGrade = int(input())
        if discussionGrade < 0 or discussionGrade > 111:
            print('******INVALID INPUT********')
            print('Input discussion grade.')
            discussionGrade = int(input())
        disGrade = discussionGrade * 0.15
    else:
        False

    while (qzGrade == None):
        # Prompt user for quiz grade.
        print('Input quiz grade.')
        quizGrade = int(input())
        if quizGrade < 0 or quizGrade > 111:
            print('******INVALID INPUT********')
            print('Input quiz grade.')
            quizGrade = int(input())
        qzGrade = quizGrade * 0.35
    else:
        False

    while (assGrade == None):
        # Prompt user for assignment grade.
        print('Input assignment grade.')
        assignmentGrade = int(input())
        if assignmentGrade < 0 or assignmentGrade > 111:
            print('******INVALID INPUT********')
            print('Input assignment grade.')
            assignmentGrade = int(input())
        assGrade = assignmentGrade * 0.5
    else:
        False
        
    # Calculate Average
    wtAvgGrade = disGrade + qzGrade + assGrade
           
    return (wtAvgGrade)
          
# Main ---------------------------------------------------------------
def main():
    # Display Header
    Header()

    # Display Welcome message
    Welcome()

    # Dictionary
    Winner = {'Brandon': 0, 'Amy': 0, 'Grace': 0, 'Ginger': 0}

    # For loop
    studentNames = ['Brandon', 'Amy', 'Grace', 'Ginger']
    for Name in studentNames:
        print('\nInput Grades for', Name,'.')
        wtAvgGrade = Grade(studentNames)
        Winner [Name] = wtAvgGrade
    
    # Max for the dictionary.    
    Max = max(Winner.items(), key=lambda item: item[1])

    # Print Results
    print('The student with the highest grade is:\t', Max)


#--- Execute -----------------------------------------------
main()
