#Print 10 random numbers in the range 1 to 100.
#Here is an example run:
# 45 79 61 47 52 10 16 83 19 12
# Each time you run your program you should get different numbers


# Import required Packages and Modules

import random

# Define the main() function
def main() -> None:
    
    for i in range(10):
        print(random.randint(1, 100), end = " ")    



# Call the main() function
if __name__ == '__main__':
    main()