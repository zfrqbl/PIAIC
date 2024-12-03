# Write a program to print terms in the Fibonacci sequence as long as the terms are less than 10,000

# Create the main() function
def main() -> None:

# Initialize the Fib(0) and Fib(1) terms  
    fib0:int = 0
    fib1:int = 1

# Generate the Fibonacci sequence by adding Fib(0) and Fib(1)
# and assign the result to Fib(2)
    
    while fib0 < 10000:
        print(fib0, end=" ")
        fib2:int = fib0 + fib1
        fib0 = fib1
        fib1 = fib2
# Call the main() function

if __name__ == '__main__':
    main()
