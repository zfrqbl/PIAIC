# Define the main() function
def main() -> None:
# Prompt the user to enter a temperature in Fahrenheit
    fahrenheit: float = float(input("Enter a temperature in Fahrenheit: "))
# Calculate the temperature in Celsius
    celsius: float = (fahrenheit - 32) * 5 / 9
# Print the temperature in Celsius
    print(f"The temperature in Celsius is {round(celsius, 2)} degrees.")


# Call the main() function.
if __name__ == '__main__':
    main()
