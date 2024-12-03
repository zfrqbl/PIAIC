
# Create an add_three_copies(...) function which takes a list and some data 
# Adds three copies of the data to the list. 
# Enter a message to copy: Hello world!
# List before: []
# List after: ['Hello world!', 'Hello world!', 'Hello world!']

def add_three_copies(list, data):
    list.append(data)
    list.append(data)
    list.append(data)
    return list

# Create the main() function
def main() -> None:
    myList:list = []
    message:str = input("Enter a message to copy: ")
    print("List before: ", myList)
    add_three_copies(myList, message)
    print("List after: ", myList)

# Call the main ()function
if __name__ == "__main__":  
    main()  
