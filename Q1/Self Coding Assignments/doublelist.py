# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# create the main() function
def main() -> None:
    numbers: list = [1, 2, 3, 4,5,6,7,8,9,10]


    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    print(*numbers)


# call the main() function
if __name__ == "__main__":  
    main()  