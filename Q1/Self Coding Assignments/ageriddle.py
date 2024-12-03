# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.



# Define the main() function
def main() ->None:

    anton:int = 21
    beth:int = anton + 6
    chen:int = beth + 20
    drew:int = chen + anton
    ethan:int = chen
    print(f"Anton is {anton} years old.\nBeth is {beth} years old.\nChen is {chen} years old.\nDrew is {drew} years old.\nEthan is {ethan} years old.")


# Call the main() function.
if __name__ == '__main__':
    main()
