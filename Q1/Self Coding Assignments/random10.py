# Print 10 random numbers in the range 1 to 100.

# Import the random module
import random   

# Define the main() function
def main() -> None:
    for i in range(10):
        print(random.randint(1, 101), end=" ")
              

# Call the main() function
if __name__ == "__main__":
    main()