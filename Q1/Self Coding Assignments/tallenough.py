# Write a program which asks the user how tall they are 
# Prints whether they're taller than a pre-specified minimum height.
# Assume for now that the minimum height is 50 of whatever height unit you'd like

# Define the main() function
def main() -> None:
    # Prompt the user to enter their height
    height: int = int(input("Enter your height: "))
    # Check if the user is tall enough
    if height >= 50:
        # Print "That's tall enough!"
        print("That's tall enough!")
    else:
        # Print "That's not tall enough."
        print("That's not tall enough.")    

# Call the main() function      
if __name__ == "__main__":
    main()  

