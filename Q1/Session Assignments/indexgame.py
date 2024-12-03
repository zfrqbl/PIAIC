# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

#Accessing Elements:
#Write a function that:

#Accepts a list and an index as inputs.
#Returns the element at the specified index.
#If the index is out of range, return an appropriate message.

#Modifying Elements:
#Write a function that:

#Accepts a list, an index, and a new value as inputs.
#Replaces the element at the specified index with the new value.
#If the index is out of range, return an appropriate message.

#Slicing the List:
#Write a function that:

#Accepts a list, a start index, and an end index as inputs.
#Returns a new list containing the elements from the start index up to (but not including) the end index.
#Handles cases where the indices are out of range.

#Game Interaction:
#Create a simple text-based game that:

#Prompts the user to select an operation (access, modify, slice).
#Asks for the necessary inputs (index, new value, etc.).
#Displays the result and the updated list.



# Define the accessElement() function
def accessElement(myList:list) -> None:
    print(*myList)
    index:int = int(input("\nEnter an index: "))

# Check if the index is valid   
    if index < 0 or index >= len(myList):
        print("\nInvalid index. Please enter a valid index.")
    else:
        print(myList[index])

# Define the modifyElement() function
def modifyElement(myList:list) -> None:    
    print(*myList)
    index:int = int(input("\nEnter an index: "))
# Check if the index is valid     
    if index < 0 or index >= len(myList):
        print("\nInvalid index. Please enter a valid index.")
    else:
        value = input("\nEnter a new value: ")
        myList[index] = value
        print("Element modified successfully.\n") 
        print(f"The new list is: {myList}")

# Define the sliceList() function
def sliceList(myList:list) -> None: 
    print(*myList)    
    print("Please note that the list index starts from 0. The end index is exclusive.")   
    start:int = int(input("\nEnter a start index: ")) 
    end:int = int(input("\nEnter an end index: "))

# Check if the index is valid 
    if start < 0 or start >= len(myList) or end < 0 or end >= len(myList):
        print("\nInvalid index. Please enter valid indices.")
    else:
        slicedList = myList[start:end]
        print(slicedList)   


# Define the main() function
def main() -> None:
# Create a list with at least 5 different elements
    myList:list = ["apple", 1, "z", 2.2, 2]

# Get the user prompt
    print("Enter a to access an element in the list\nEnter m to modify an element in the list\nEnter s to slice the list\n")
    userPrompt = input("Enter a, m, or s: ").lower()

# Call the appropriate function based on the user prompt
    if userPrompt == "a":
        accessElement(myList)
    elif userPrompt == "m":
        modifyElement(myList)
    elif userPrompt == "s":
        sliceList(myList)
    else:
        print("Invalid input. Please enter a, m, or s.")



# Call the main() function
if __name__ == '__main__':
    main()