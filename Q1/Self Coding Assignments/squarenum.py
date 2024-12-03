# Ask the user for a number and print its square (the product of the number times itself).

# 4.0 squared is 16.0


# Define the main() function
def main() -> None:
    # Prompt the user to enter a number
    number: float = float(input("Enter a number: "))
    # Calculate the square of the number
    square: float = number * number
    # Print the result
    print(f"{number} squared is {square}")


# Call the main function
if __name__ == '__main__':
    main()