# Write the get_user_data() function. 
# This function will:
# Ask the user for their first name and stores it in a variable

# Ask the user for their last name and stores it in a variable

# Ask the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked


# write the get_user_data() function
def get_user_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    return first_name, last_name, email 


# write the main () function
def main():
    x=get_user_data()
    print(f"Received the following data from the user: {x}")

# call the main() function      
if __name__ == "__main__":
    main()      