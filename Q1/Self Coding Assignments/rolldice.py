# Simulate rolling two dice, and prints results of each roll as well as the total.

# Import the random module
import random

# Define the main() function
def main() -> None:
    dice1:int = random.randint(1, 6)
    dice2:int = random.randint(1, 6)
    total:int = dice1 + dice2
    print(f"Dice 1: {dice1} Dice 2: {dice2} Total: {total}")

# Call the main() function

if __name__ == '__main__':
    main()

