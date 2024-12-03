# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Define the main() function
def main() -> None:

    # Define C as the speed of light
    C: int = 299792458

    # Prompt the user to enter a mass
    mass: float = float(input("Enter a mass: "))
    # Calculate the energy
    energy: float = mass * C **2
    # Print the numbers
    print(f"e = m * c**2\nmass = {mass}\nC = {C}\nThe energy is {energy}")





# Call the main() function

if __name__ == '__main__':
    main()

