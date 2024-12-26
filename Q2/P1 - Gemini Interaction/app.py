# PIAIC Q2 - Project 1
# LangChain Gemini Interaction
# Problem Statement

#Create a simple LangChain Colab Notebook that uses the Google Gemini Flash 2.0 model to answer user questions.

# Next,

# Experiment with Prompts: Add more prompt templates to see how the model responds.
# Add Memory: Use LangChain’s memory feature to make the interaction multi-turn.
# Integrate Tools: Extend the chain to include tools like database queries or APIs.
# Explore Gemini Features: Adjust temperature, max tokens, and other parameters to optimize responses.






# Import the required libraries and modules
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the Google API key from the environment variable
api_key = os.getenv('GOOGLE_API_KEY_1')

# Check if the API key is loaded
if not api_key:
    raise ValueError("Google API key is not set. Ensure your .env file contains 'GOOGLE_API_KEY_1'.")

# Set the parameters of the LLM object for Google Gemini Flash
llm = ChatGoogleGenerativeAI(
    api_key=api_key,
    model="gemini-1.5-flash",
    temperature=0.7
)

# Set up memory for conversation
# this object will use the combined_input as a key to track the conversation
# crtitical for avoiding the expected one key error 
memory = ConversationBufferMemory(input_key="combined_input")  

# Prompt the user for the LLM's role
role = input("What role should the LLM assume? > ")
addDetails = input("Do you want to add any additional details? > ")

# Define the prompt template
template = '''You are a helpful assistant acting as a {role}. Use these details for further information about the role: {addDetails}. Answer the following question:
{combined_input}
{history}
'''

# Create the PromptTemplate object and load it with the template
prompt_template = PromptTemplate(
    input_variables=["role", "addDetails", "combined_input", "history"],
    template=template
)

# Create the LLM chain with memory
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    memory=memory
)
# Conversation loop
print("\nConversation started. Type 'exit' to end.\n")

while True:
    try:
        # Get user question
        question = input("You: ")
        if question.lower() == 'exit':
            print("Ending conversation. Goodbye!")
            break

        # Combine role and question into a single input
        combined_input = f"Role: {role}\nQuestion: {question}"

        # Get LLM response
        llm_response = llm_chain.predict(
            role=role,
            addDetails=addDetails,
            combined_input=combined_input
        )

        # Display the response
        print(f"\nGemini: {llm_response}\n")

        # Optionally display conversation history
        #this process splits the memory buffer into lines (ending on new line characters)
        #Next, it prints each line in the conversation history
        print("\nConversation history so far:\n")
        for i, entry in enumerate(memory.buffer.split("\n")):
            print(f"{i + 1}: {entry}")

    except Exception as e:
        print(f"An error occurred: {e}")
