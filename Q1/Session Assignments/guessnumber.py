# Sample Run
# Guess My Number

#I am thinking of a number between 0 and 99... 
# Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

# Import Required Packages and Modules  

import random

# Define the main() function
def main() -> None:

# Select a random number between 0 and 99
    number:int = random.randint(0, 99)   
    #print(number)
# Get the user's guess   
    print("I am thinking of a number between 0 and 99...")
    userGusess:int = int(input("Enter a guess: "))

# Process the userGuess
    while userGusess != number:
        
        if userGusess < number:
            print("Your guess is too low")
            userGusess:int = int(input("\nEnter a guess: "))
        elif userGusess > number:
            print("Your guess is too high")
            userGusess:int = int(input("\nEnter a guess: "))
        
    print("Congrats! The number was: ", number)
            

# Call the main() function
if __name__ == '__main__':
    main()