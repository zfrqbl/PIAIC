# Pythagorean Theorem
# BC ** 2 = AB ** 2 + AC ** 2

# Here's a sample run of the program:

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0



# Define the main() function
def main() -> None:

    # Prompt the user to enter the lengths of each side of a triangle
    AB: float = float(input("Enter the length of AB: "))
    AC: float = float(input("Enter the length of AC: "))
    # Calculate the length of BC (the hypotenuse)
   
    BC: float = (AB ** 2 + AC ** 2) ** 0.5
    # Print the result
    print(f"The length of BC (the hypotenuse) is: {BC}")

# Call the main() function

if __name__ == '__main__':
    main()

