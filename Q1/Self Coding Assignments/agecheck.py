# Write the adult() function 
# which returns True if the function takes an age that is greater than or equal to ADULT_AGE. 
# If the function takes an age less than ADULT_AGE, return False instead.

# Define the Global variable 
ADULT_AGE = 21

# Write the adult() function

def adult(age):
    if age < ADULT_AGE:
        return False
    return True  

# write the main() function 

def main():
    age = int(input("Enter your age: "))
    if adult(age):
        print("You are an adult.")
    else:
        print("You are not an adult.")         

# call the main function

if __name__ == "__main__":
    main()  
