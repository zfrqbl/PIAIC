# Write a program that reads a year from the user and tells whether a given year is a leap year
# Tree criteria must be checked to identify leap years:

# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.
#Your code should then print either "That's a leap year!" or "That's not a leap year."


# Define the main() function
def main() -> None: 
    # Prompt the user to enter a year
    year: int = int(input("Enter a year: "))
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Print "That's a leap year!"
        print("That's a leap year!")
    else:
        # Print "That's not a leap year."
        print("That's not a leap year.")    

# Call the main() function      

if __name__ == "__main__":
    main()  