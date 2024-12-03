# Write a Python program that takes two integer inputs from the user and calculates their sum.
# The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message

# Define the main function
def main():
    # Prompt the user to enter the first number
    num1 = input("Enter the first number: ")
    # Convert the input to an integer
    num1 = int(num1)
    # Prompt the user to enter the second number
    num2 = input("Enter the second number: ")
    # Convert the input to an integer
    num2 = int(num2)
    # Calculate the sum of the two numbers
    total = num1 + num2
    # Print the total sum with an appropriate message
    print(f"The sum of {num1} and {num2} is {total}")

# Call the main function                
if __name__ == "__main__":
    main()  