# Create the function shorten(lst) which removes elements from the end of a list (lst)
#  Prints each item it removes until lst is MAX_LENGTH items long. 
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. 
# 

# Write the shorten() function

def shorten(lst, maxLength):
    while len(lst) > maxLength:
        x =lst.pop()
        print(x)

# Create the main() function

def main() -> None:
    lst: list = [1, 2, 3, 4, 5,6,7,8,9,10]
    maxLength = int(input("Please type the cut off index>  "))
    shorten(lst, maxLength)
    print(lst)


# Call the main() function
if __name__ == "__main__":
    main()  