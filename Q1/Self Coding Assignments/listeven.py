# Write the count_even(lst) that first 
# populates a list by prompting the user for integers until they press enter 
# and then prints the number of even numbers in the list.

# Write the count_even() function
def count_even(lst) -> int:
    lst:list = []
    while True:
        num:str = input("Enter a number: ")
        if num == "":
            break
        lst.append(int(num))
    
# Processing the lst list and counting the number of even numbers    
    count = 0
    print(f"\nList: {lst}\n")
    for i in lst:
        if i % 2 == 0:
            count += 1
         
    return count


# Write the main() function
def main() -> None:
    print(f"There are {count_even([])} even numbers in the list\n")

# Call the main() function
if __name__ == "__main__":
    main()