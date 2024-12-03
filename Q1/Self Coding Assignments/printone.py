# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. 


# Write the print_ones_digit() function
def print_ones_digit(num):
    print(num % 10) 

# Write the main() function
def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)   

# Call the main() function  
if __name__ == "__main__":
    main()    
