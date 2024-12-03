# Develop a game called High-Low.
# Here is how it's played:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. 
# You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.


# Import required packages and modules

import random

# Define the Global Variables

TOTALTURNS:int = 0
COMPUTERNUMBER:int


# Define the main() function

def main() -> None:

# Ask the users how many rounds they wish to play

# Declare USERSCORE as a local variable to avoid conflict within the main() function
    USERSCORE:int = 0 
    TOTALTURNS = int(input("How many rounds would you like to play? "))

    for i in range(TOTALTURNS):
        print(f"Round {i + 1}")
        COMPUTERNUMBER = random.randint(1, 100)
        #print(COMPUTERNUMBER)
# Get the user input 
        userGuess = int(input("Enter your guess: ")) 

# Process the user's guess 
# Check if the user's guess is higher or lower than the computer's number
        if userGuess > COMPUTERNUMBER:
            print("Your guess is too high")
            print(f"Your score is: {USERSCORE}\n")    

        elif userGuess < COMPUTERNUMBER:    
            print("Your guess is too low")
            print(f"Your score is: {USERSCORE}\n")    

        else:                     
            USERSCORE += 1
            print("Congrats! You got it right!")
            print(f"Your score is: {USERSCORE}")    

    print("Game Over")  
    print(f"Your final score is: {USERSCORE}")











# Run the main() function
if __name__ == '__main__':
    main()  
