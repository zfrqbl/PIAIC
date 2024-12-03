# Create the function get_first_element(lst)
# Which takes in a list lst as a parameter
# Prints the first element in the list. 
# 

# Write the get_first_element() function
def get_first_element(lst):
    print(lst[0])   

# Create teh main() function
def main() -> None:
    lst = [1, 2, 3, 4, 5]
    get_first_element(lst)

# Call the main() function  
if __name__ == "__main__":  
    main()  