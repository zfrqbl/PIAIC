# Write a function that takes two numbers and finds the average between the two.

# Define the average() function
def average(num1, num2) -> float:
    return (num1 + num2) / 2    

# Define the main() function
def main():
    # Prompt the user to enter the first number
    num1: float = float(input("Enter the first number: "))
    # Prompt the user to enter the second number
    num2: float = float(input("Enter the second number: "))
    # Calculate the average of the two numbers
    avg: float = average(num1, num2)
    # Print the average with an appropriate message
    print(f"The average of {num1} and {num2} is {avg}")

# Call the main() function
if __name__ == "__main__":
    main()  