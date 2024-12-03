# Write a function that takes a list of numbers and returns the sum of those numbers.

# Create teh main() function    
def main() -> None:
    numbers: list = [1, 2, 3, 4, 5]
    # Use the one-liner
    # print(sum(numbers)) 
    sumList: int = 0
    for i in range(len(numbers)):
        sumList += numbers[i]
    print(sumList)

# Call the main() function
if __name__ == "__main__":  
    main()  