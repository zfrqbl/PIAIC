# Write the print_multiple(message, repeats), function
# which takes as parameters a string message to print
# and an integer repeats number of times to print message. 


# Write the print_multiple() function   
def print_multiple(message, repeats):
    for i in range(repeats):
        print(message)
    
    print(f"\n{message * repeats}")
    
# Write the main() function
def main():
    # Call the print_multiple() function
    message = input("Enter a message: ")
    repeats = int(input("Enter the number of times to repeat the message: "))
    print_multiple(message, repeats)

# Call the main() function
if __name__ == "__main__":
    main()      