# This program counts from 1 to 100 and using a counting() function
# This function stops when another function done() returns true. 

# The counting function runs a for loop from 1 to 100 and prints each number
# until the done() function returns true. 

# The done() function uses a random number between 1 and 10 to set a for loop.
# When this for loop is complete, the done() function returns true.

# Import the required modules
import random   
import time

# Define the done() function with an empty for loop
def done() -> bool:
    x = random.randint(1, 10)
    print(f"x is {x}")
    time.sleep(x)
    return True



# Define the counting() function
def counting() -> None:
    for i in range(1, 101):
        print(i)
        if done():
            break
# Define the main() function         
def main() -> None:
    counting()           
    print("Done!")

 
 # Call the main() function
if __name__ == '__main__':
    main()  

