################################################################
###########            ROCK-PAPER-SCISSORS           ###########
###########            by Miguel Pedraza             ###########
################################################################

# -----------------MODULES----------------- 

# Module to generate random number
import random

# -----------------END MODULES-----------------

# When we find the winner we save it in here
winner = ""

# Variable to check if the game is still going
stillPlaying = True

# Counter for the user
userRoundCount = 0

# Counter for the computer
computerRoundCount = 0 

# -----------------FUNCTIONS-----------------

# Function to star playing
def play():

    # Global variables
    global stillPlaying
    global winner

    print("***********************************************************************************")
    print("**                          WELCOME TO ROCK PAPER SCISSORS                       **")
    print("**                                by Miguel Pedraza                              **")
    print("***********************************************************************************")
    print("")
    print("INSTRUCTIONS: Type rock, paper or scissors and try to beat the computer. Good luck!")
    print("Remember whoever wins 3 rounds first will win the game!")
    print("")

    # Loop to know if we are still playing and keep asking the user for an input until someone wins 3 rounds
    while stillPlaying:
        userChoice = playersChoice()
        compuChoice = computerChoice()
        determineWinner(userChoice, compuChoice) 

    # Once either the user or the computer has won 3 rounds we determine the winner
    if winner == "User":
        print("You won the game! Nice work!")
    else:
        print("The " + winner + " won the game! Better luck next time!")

# Funtion to ask for player´s choice
def playersChoice():
    # Rock Paper Scissors variable from the user 
    rpsUser = input("Choose rock, paper or scissors: ")

    # While loop to keep asking until user types one of the correct options
    while True:
        if rpsUser == "rock" or rpsUser == "paper" or rpsUser == "scissors":
            break
        else:
            rpsUser = input("Invalid choice. Choose rock, paper or scissors: ")

    # We return the user choice
    return rpsUser

# Function to determine computer´s choice
def computerChoice():
    # Generate a random int number from 1-3 to assign it to rock, paper or scissors
    n = random.randint(1, 3)

    # Conditions to assign the computer choice
    if n == 1:
        rpsComputer = "rock"
    elif n == 2:
        rpsComputer = "paper"
    else:
        rpsComputer = "scissors"

    # We return the computer choice
    return rpsComputer
    
# Function to determine who won 
def determineWinner(userChoice, compuChoice):

    # Global variables
    global winner
    global stillPlaying
    global userRoundCount 
    global computerRoundCount 
    
    # Conditions to see who wins and count how many rounds have they won
    if userChoice == "rock":
        if compuChoice == "rock":
            print("Computer choose rock. That's a tie!")
        elif compuChoice == "paper":
            print("Computer choose paper. Computer won this round!")
            computerRoundCount += 1
        else:
            print("Computer choose scissors. User won this round!")
            userRoundCount += 1
    elif userChoice == "paper":
        if compuChoice == "rock":
            print("Computer choose rock. User won this round!")
            userRoundCount += 1
        elif compuChoice == "paper":
            print("Computer choose paper. That's a tie!")
        else:
            print("Computer choose scissors. Computer won this round!")
            computerRoundCount += 1
    else:
        if compuChoice == "rock":
            print("Computer choose rock. Computer won this round!")
            computerRoundCount += 1
        elif compuChoice == "paper":
            print("Computer choose paper. User won this round!")
            userRoundCount += 1
        else:
            print("Computer choose scissors. That's a tie!")

    # Condition to check if either the computer or the user won 3 rounds
    if userRoundCount == 3:
        winner = "User"
        stillPlaying = False
    elif computerRoundCount == 3:
        winner = "Computer"
        stillPlaying = False

# -----------------END FUNCTIONS-----------------

# -----------------MAIN-----------------

# Call the play function and start 
play()