# Write the get_name() function that takes the user's first and last name as parameters
# and returns a string with the user's full name.


# Write the get_name() function
def get_name(first_name, last_name):
    return f"{first_name} {last_name}"  

# Create the main() function
def main():
    # Get the user's first name
    first_name = input("Enter your first name: ")
    # Get the user's last name
    last_name = input("Enter your last name: ")
    # Call the get_name() function
    full_name = get_name(first_name, last_name)
    # Print the user's full name
    print(f"Your full name is {full_name}")

# Call the main() function  
if __name__ == "__main__":
    main()  