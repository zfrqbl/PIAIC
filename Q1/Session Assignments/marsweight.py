# An Earthling's weight on Mars is 37.8% of their weight on Earth. 
# Write a Python program that prompts an Earthling to enter their weight on Earth
# Print their calculated weight on Mars.
# The output should be rounded to two decimal places when necessary. 
# 3.1415926 is rounded to 2 decimal places which is 3.14.


# Define the main() function
def main() -> None:
    earthling_weight = float(input("Enter your weight in kilograms: "))
    mars_weight = earthling_weight * 0.378
    #print(f"Your weight on Mars is {mars_weight:.2f} pounds")
    print(f"Your weight on Mars is {round(mars_weight,2)} pounds")

# Call the main() function
if __name__ == '__main__':
    main()  