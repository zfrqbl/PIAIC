# Write a function num_in_stock() which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. 

# The main() will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit in stock

# Print the number which are in stock

# Print "This fruit is not in stock." if there are none of that fruit in the inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.


# write the num_in_stock() function
def num_in_stock(fruit):
    if fruit == "pear": 
        return 1000
    elif fruit == "banana":
        return 500
    elif fruit == "apple":
        return 200
    else:
        return "This fruit is not in stock."

# write the main() function 
def main():
    fruit = input("Enter a fruit: ")    
    result = num_in_stock(fruit)
    print(result)

# call the main() function
if __name__ == "__main__":
    main()  
    
        