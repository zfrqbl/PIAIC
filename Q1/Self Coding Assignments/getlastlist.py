# Create the function get_last_element(lst) which takes in a list lst as a parameter
# Prints the last element in the list. 
# 

# Write the get_last_element() function 
def get_last_element(lst):
    print(lst[-1])  

# Create the main() function
def main() -> None:
    lst = [1, 2, 3, 4, 5]
    get_last_element(lst)

# Call the main() function
if __name__ == "__main__":  
    main()  
