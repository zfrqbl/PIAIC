# Write the make_sentence(word, part_of_speech) function which will take a string word and an integer part_of_speech
# and, depending on the part of speech, place the word into one of three sentence templates

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"

# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"

# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!"



# Write the make_sentence() function
def make_sentence(word, part_of_speech) -> None:
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!") #return f"I am excited to add this {word} to my vast collection of them!"
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!") 


# Write the main() function      
def main():
    word = input("Please enter a word: ")
    part_of_speech = int(input("Please enter a part of speech. \nType 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

# Call the main() function  
if __name__ == "__main__":
    main()  