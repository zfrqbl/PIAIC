# Ask the user for two numbers, one at a time
# Print the result of dividing the first number by the second
# Also the remainder of the division.

# Here's a sample run of the program

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2


# Define the main() function
def main() -> None:

    # Prompt the user to enter an integer to be divided
    num1:int = int(input("Please enter an integer to be divided: "))
    # Prompt the user to enter an integer to divide by
    num2:int = int(input("Please enter an integer to divide by: "))
    # Calculate the result of the division
    result:int = num1 // num2
    # Calculate the remainder of the division
    remainder:int = num1 % num2
    # Print the result
    print(f"The result of this division is {result} with a remainder of {remainder}")

# Call the main() function

if __name__ == '__main__':
    main()

