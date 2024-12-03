# Create a list called fruit_list that contains the following fruits: 
# # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Print the length of the list.
# Add 'mango' at the end of the list. 
# Print the updated list.

# Define the main() function
def main() -> None:
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# Print the length of the list    
    print(len(fruit_list))

# Add 'mango' at the end of the list.     
    fruit_list.append('mango')

# Print the updated list in a clean way.
    print(*fruit_list)

# Call the main() function    
if __name__ == '__main__':
    main()  
