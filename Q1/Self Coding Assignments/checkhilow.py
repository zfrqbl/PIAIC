# Write the def in_range(n, low, high) function which takes in 3 integers
# Returns True if n is between low and high, inclusive.

# Write the in_range() function
def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    else:
        return False

# Write the main() function
def main():
    num:int = int(input("Enter a number: "))
    low:int = int(input("Enter a low number: "))
    high:int = int(input("Enter a high number: "))  

    print(in_range(num, low, high))

# Call the main() function
if __name__ == "__main__":
    main()  