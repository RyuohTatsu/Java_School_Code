# Python code
# This program will populate an array and then manipulate it.
# Developer: Brian Walters CMIS102/7384
# Developed: April 26, 2023
# Riddles obtained from Kidspot (https://www.kidspot.com.au/parenting/things-to-do/10-riddles-that-play-on-words/news-story/38308fcc7c41a224ade5d3d99da64ac4)
 

# Main ---------------------------------------------------------------
def main():
    # Display Header
    Header()

    # Display Welcome message
    Welcome()

    # Call Functions
    # Initialize list.
    answers = []
    
    # Ask Riddles
    answers = Riddles(answers)

    # Correct Answers
    answers = CorrectAns(answers)

    #Display output
    answers = Output(answers)

# Functions -----------------------------------------------------------------------------------------

# Header
def Header():
    print('Name: Brian Walters')
    print('Week 7 Discussion: Playing with an Array.')
    print('CMIS 102/7384')
    
# Welcome ------------------------------
def Welcome():
   # This function displays the Welcome message
   print('\nWelcome to B\'s Riddle Game.')
   print('I will ask you 5 riddles and you guess the answers.')
   print('After you aswer all 5 riddles I will let you know if you were correct or not.')
  
# Ask Riddles -----------------------------
def Riddles(answers):
    # Ask 5 riddles in a loop and put the answers in an array.

    # Initialize loop to ask the riddles.
    r = 1
    while r > 0:
        if r == 1:
            answers.append(input('\n1. What type of cheese is made backwards?\n'))
            answers.append(input('2.  am the beginning of the end, and the end of time and space. I am essential to creation, and I surround every place. What am I?\n'))
            answers.append(input('3. What five-letter word becomes shorter when you add two letters to it?\n'))
            answers.append(input("4. When you have me, you feel like sharing me. If you do share me, you don't have me. What am I?\n"))
            answers.append(input('5. I am an insect. The first part of my name is the name of another insect. What am I?\n'))
            r = r - 1
    return answers

# Answers ----------------------------
def CorrectAns(answers):
    # Changes the answers in the array to "Correct" or "Incorrect".

    for i in range(len(answers)):
        if answers[i] in ['edam', 'e', 'short', 'secret', 'beetle']:
            answers[i] = 'Correct'
        else:
            answers[i] = 'Incorrect'
    return answers
    
# Output
def Output(answers):
    # Displays the modified answers
    for answer in answers:
        print(answer)

    input('\nHit any key to see the correct answers.\n')
    if 'answer':
        print('1. edam \n2. e \n3. short \n4. secret \n5. beetle')

    print('\n****************Thanks for playing. Please come again.******************')
    print('\nRiddles obtained from kidspot (https://www.kidspot.com.au/parenting/things-to-do/10-riddles-that-play-on-words/news-story/38308fcc7c41a224ade5d3d99da64ac4)')

          
#--- Execute -----------------------------------------------
main()
