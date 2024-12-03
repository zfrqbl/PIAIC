# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. 

# Here's a sample run of the program

# Please type the following affirmation: 
# I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

# Define the main() function
def main() -> None:
    affirmation: str = input("Please type the following affirmation: I am capable of doing anything I put my mind to. ")
    
# Check if the user input is correct    
    while affirmation != "I am capable of doing anything I put my mind to.":
        affirmation = input("Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. ")
    print("That's right! :)" )

# call the main() function  
if __name__ == "__main__":  
    main()  