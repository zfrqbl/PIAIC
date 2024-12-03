# Write a function getoddeven() that takes all integers from 1 to 100 as parameters and prints the odd numbers followed by the even numbers.
# Use a for loop and a conditional statement to check if the number is odd or even.

# The final output should look like this:
# 1 odd 2 even 3 odd ...... 100 even


# Write the getoddeven() function
def getoddeven() -> None:
    for i in range(1,101):
        if i % 2 == 0:
            print(i, "even ")
        else:
            print(i, "odd ") 

# Define the main() function
def main() -> None:
    getoddeven()  

# Call the main() function
if __name__ == "__main__":
    main()    
