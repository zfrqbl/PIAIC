# Create a dictionary based phonebook
# The code has the following three functions
# Add: This fucntion adds a contact to the phonebook
# Remove: This function removes a contact from the phonebook
# View: This function views all the contacts in the phonebook

# Create the add_contact() function
def add_contact(phonebook) -> None:
    name:str = input("Enter the name: ")
    phone:str = input("Enter the phone number: ")
    phonebook[name] = phone
    print("Contact added successfully")

# Create the remove_contact() function  
def remove_contact(phonebook) -> None:
    name:str = input("Enter the name: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact removed successfully")
    else:
        print("Contact not found")

# Create the view_contacts() function
def view_contacts(phonebook) -> None:
    for name, phone in phonebook.items():
        print(f"{name} --- {phone}")


# Create a main() function
def main() -> None:

# This is the main dictionary
    phonebook = {}
    while True:
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. View all contacts")
        print("4. Exit")
      
        userChoice = input("\nEnter your choice >  ")
        if userChoice == "1":
            add_contact(phonebook)
        elif userChoice == "2":
            remove_contact(phonebook)
        elif userChoice == "3":
            view_contacts(phonebook)
        elif userChoice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")


# Call the main() function
if __name__ == '__main__':
    main()  
            