# Write a program which asks the user what their favorite animal is
# Always responds with "My favorite animal is also ___!"




# Define the main function
def main() -> None:
    # Prompt the user to enter their favorite animal
    favorite_animal: str = input("What is your favorite animal? ")
    # Print a message with the user's favorite animal
    print(f"My favorite animal is also {favorite_animal}!") 

# Call the main function                        
if __name__ == "__main__":
    main()  