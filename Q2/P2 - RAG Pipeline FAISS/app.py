# This RAG project uses Google Generative AI, LangChain, and FAISS. 
#Create a simple LangChain RAG Colab Notebook that uses the Google Gemini Flash model to answer user questions from the document provided. T
# his Retrieval-Augmented Generation (RAG) system uses LangChain with Google Gemini Flash and FAISS. 
# This system will retrieve relevant context from a vector database and use that context to generate a more accurate and informed response from the Gemini model.

#I choose FAISS because it doesn't need an API key, a problem that I faced with Pinecone.
# I also decided to use the logging library for status output because I saw a YT video showing the benefits of teh library over teh print() statements.


import os
import sys
import logging
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging for imports
logging.info("Imports Done successfully.")


# Load the environment variables from the .env file
load_dotenv()

# Access the Google API key from the environment variable
api_key = os.getenv('GOOGLE_API_KEY')

# Check if the Google API key is loaded
if not api_key:
    logging.error("Google API key is not set. Ensure your .env file contains 'GOOGLE_API_KEY_1'. Exiting.")
    sys.exit(1)  # Exit with a non-zero code to indicate an error
else:
    logging.info("Google API key loaded successfully.")



# Configure logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function Definition
# This function creates and returns a RAG pipeline using FAISS
# In Step #1, the TextLoader() loads the document
# In Step #2, RecursiveCharacterTextSplitter() creats chunks by breaking at newline and other characters  
# in Step #3, embeddings are created and uploaded to FAISS
# In Step #4,  the LangChain RetrievalQA chain is created

def create_rag_pipeline(document_path: str):
    
    try:
        # Step #1. Load the document
        loader = TextLoader(document_path)
        documents = loader.load()
        logging.info(f"Loaded {len(documents)} documents.")

        # Step #2. Split the document into chunks using RecursiveCharacterTextSplitter
       # The chunks are split by double newline, newline, space, then character       
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,  
        chunk_overlap=50, 
        separators=["\n\n", "\n", " ", ""],  
        length_function=len,
         )
        
        # The docs list conatins the chuncks 
       
        docs:list = text_splitter.split_documents(documents)
        logging.info(f"Split document into {len(docs)} chunks.")

        # Step #3. Create embeddings and store them in FAISS

        embeddings = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")
        
        # This uses the from_documents() method fro simpler uploads of the chunks and embedding model info  
       
        db = FAISS.from_documents(docs, embeddings) # Using FAISS
        logging.info("Created FAISS vector store.")

        # Step #4. Create the RetrievalQA chain

        # Create the llm object for Google Gemini
        llm = ChatGoogleGenerativeAI(
           api_key=api_key,
           model="gemini-1.5-flash",
           temperature=0.2
        )
        
        # The qa variable contains the response of the LLM that will be passed to the user

        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
        logging.info("Created RetrievalQA chain.")

        return qa

    except Exception as e:
        logging.error(f"An error occurred during pipeline creation: {e}")
        return None

# Define the main() function

def main():
    
    document_path = "turing.txt"
    if not os.path.exists(document_path):
        raise FileNotFoundError(f"Document not found: {document_path}")

# Call the create_rag_pipeline() function. 
# If there are no issues in the call, the user is asked for the question
# This question is stored in query variable.
# Next, the qa_pipeline is invoked with the query as parameter to get the LLM response.

    qa_pipeline = create_rag_pipeline(document_path)

    if qa_pipeline:
        while True:
            query = input("Enter your query (or type 'exit'): ")
            if query.lower() == "exit":
                break

            try:
                # Execute the query
                result = qa_pipeline.invoke(query)
                print(f"Answer: {result['result']}")
            except Exception as e:
                logging.error(f"Error during query execution: {e}")
                print("An error occurred while processing your query. Please check the logs.")
    else:
        print("Failed to create the RAG pipeline.")

# Run the main() function
if __name__ == "__main__":
    main()