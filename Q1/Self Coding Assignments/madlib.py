# Write a program which prompts the user for an adjective, then a noun, then a verb
# Prints a fun sentence with those words!
# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny
# Please type a noun and press enter. plant
# Please type a verb and press enter. fly

# Sample sentence
# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

# define the main() function
def main() -> None:
    adjective:str = input("Please type an adjective and press enter. ")
    noun:str = input("Please type a noun and press enter. ")
    verb:str = input("Please type a verb and press enter. ")
    sentence = f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!"
    print(sentence)

# call the main() function  
if __name__ == "__main__":  
    main()