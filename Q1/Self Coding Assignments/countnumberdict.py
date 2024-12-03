# This program counts the number of times each number appears in a list. 
# It uses a dictionary to keep track of the information.

# Define the main() function
def main() -> None:
    # Create a list of numbers
    numbers: list = [1, 1, 3, 3, 5, 6, 3, 7, 9, 10]
    # Create an empty dictionary to store the counts
    countDict: dict = {}
    # Loop through the list and count the number of times each number appears
    for number in numbers:
        if number in countDict:
            countDict[number] += 1
        else:
            countDict[number] = 1
   
   
    # Ask the user for a number and show the count
    userNumber: int = int(input("Enter a number: "))
    if userNumber in countDict:
        print(f"{userNumber} appears {countDict[userNumber]} times")
    else:
        print(f"{userNumber} does not appear in the list")
   
# Call the main() function      
if __name__ == "__main__":
    main()  