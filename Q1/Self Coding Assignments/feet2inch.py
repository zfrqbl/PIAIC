# Converts feet to inches. 
# There are 12 inches per foot.


# Define the main() function
def main() -> None:
    # Prompt the user to enter a number of feet
    feet: float = float(input("Enter a number of feet: "))
    # Calculate the number of inches
    inches: float = feet * 12
    # Print the result
    print(f"{feet} feet is {inches} inches")

    
# Call the main() function

if __name__ == '__main__':
    main()

