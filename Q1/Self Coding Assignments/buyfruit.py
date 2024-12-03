
# Write a program that loops through a dictionary of fruits, 
# prompting the user to see how many of each fruit they want to buy
# prints out the total combined cost of all of the fruits.

# Here is an example run of the program 

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# Your total is $99.5

# Define the main() function
def main() -> None:
    # Create a dictionary of fruits and their prices
    fruits:dict = {
        "apple": 1.99,
        "banana": 0.99,
        "orange": 1.49,
        "kiwi": 2.99,
        "jackfruit": 4.99
    }
    # This variable stores the total cost of the fruits
    total:float = 0

    # Loop through the dictionary 
    # and prompt the user to enter the number of each fruit
    for fruit, price in fruits.items():
        quantity = int(input(f"How many {fruit} do you want?: "))
        total += quantity * price
    # Print the total cost
    print(f"Your total is ${total:.2f}")

# Call the main() function
if __name__ == '__main__':
    main()  