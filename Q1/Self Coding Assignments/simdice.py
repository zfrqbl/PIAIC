# Simulate rolling two dice, three times. Prints the results of each die roll

# Import the required modules

import random

# Define the main() function

def main() -> None:
    for i in range(3):
        dice1:int = random.randint(1, 6)
        dice2:int = random.randint(1, 6)
        print(f"Die 1: {dice1} Die 2: {dice2}\n")   



# Call the main() function

if __name__ == '__main__':
    main()