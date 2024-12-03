#https://github.com/panaversity/learn-cloud-native-modern-ai-python/blob/main/PROJECTS/session_assignments/01_basics/00_joke_bot.md

#Write a simple joke bot. 
#The bot starts by asking the user what they want. 
#However, your program will only respond to one response: Joke.

#If the user enters Joke
#we will print out a single joke. Each time the joke is always the same

#If the user enters anything else we print out:
#Sorry I only tell jokes

#You should use the three constants:
#PROMPT (the prompt asked to the user)
#JOKE   (the joke to print out if the user enters Joke)
#SORRY  (the sorry message if the user enters anything else)

#define the constants
PROMPT = "What do you want?"
JOKE = "Knock knock"
SORRY = "Sorry I only tell jokes"

#define the function tellJoke()

def tellJoke() -> None:
    print(JOKE)

#define the function main()
def main() -> None:
    print(PROMPT)
    user_input = input().strip().lower()
    if user_input == "joke":
        tellJoke()
    else:
        print(SORRY)

# Call the main() function
if __name__ == '__main__':
    main()