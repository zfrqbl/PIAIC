# Write a greet(name) function
# which takes as input a string name and prints a greeting

# Define the greet() function
def greet(name):
    print(f"Hello, {name}!")

# Write teh main() function
def main():
    # Get the user's name
    name = input("Enter your name: ")
    # Call the greet() function
    greet(name)

# Call the main() function  
if __name__ == "__main__":
    main()  