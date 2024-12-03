# Write the print_divisors(num) function
# which takes in a number and prints all of its divisors
#  (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division).


# Write the print_divisors() function
def print_divisors(num):
    divList:list = []
    for i in range(1, num + 1):
        if num % i == 0:
            divList.append(i)
    print(f"The divisors of {num} are: ")
    print(*divList)

# Write the main() function     
def main():
    num = int(input("Enter a number: "))
    print_divisors(num) 

# Call the main() function
if __name__ == '__main__':
    main()  
