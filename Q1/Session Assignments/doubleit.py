# Write a program that asks a user to enter a number. 
# Your program will then double that number and print out the result. 
# It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:

# 4 8 16 32 64 128

# Define the doubleit() function that doubles the user input and returns the result
def doubleit(number) -> int:
    number = number * 2
    return number 


# Define the main() function
def main() -> None:
    number:int = int(input("Enter a number: "))
    print(number, end = " ")
    while number < 100:
        number = doubleit(number)
        print(number, end = " ")
# Call the main() function
if __name__ == '__main__':
    main()
