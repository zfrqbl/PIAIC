# Import the required liraries and modules


from langchain_google_genai import ChatGoogleGenerativeAI

import time
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
import math


# Define the PI Constant 
PI = math.pi

# Define the E Constant 
E = math.e


# Load the Google Gemini API key
GOOGLE_API_KEY = "a"

# Initialize the Google Generative AI LLM   
llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp", api_key = GOOGLE_API_KEY, temperature=0.0)

# Define tool defintions

# Tool #1: Define the get_expression_type function
def get_expression_type(user_input:str) -> str:

  '''
  This function takes the user input, asks the LLM for the type of expression, and returns the results.

  Args:
      user_input (str): The user input string.
  Returns:
      str: The type of expression.

  '''

  # Define the prompt template
  template:str = '''
  You are a helpful maths expert.
  You will take the expression {user_input} and tell me the type of expression in a single word.
  Please double-check your response because it wil be used as inout for a series of agent actions.
  If you determine that the user_input is not a mathematical expression of any kind, return "NA".

  if you need to use pi constant, use the value {PI}
  if you need to use e constant, use the value {E}

  in case of a word problem (like " how much is 5 plus 3" and " Find the mean of 2, 4, 6, 8, 10"), 
  extract the numbers and relevant information, and use them as input for the agent actions.
  Make sure no string is included in the data passed to tools.


  '''

# Create the PromptTemplate object and load it with the template
  prompt_template = PromptTemplate(input_variables=["user_input, PI, E"], template=template)


# Create the LLM chain with memory


  chain = prompt_template | llm | StrOutputParser()
  user_input = f"{user_input}"
  input = {"user_input": user_input}
  try:
    llm_response = chain.invoke(input)
    return llm_response.strip()
  except Exception as e:
      print(f"Error in LLM call: {e}")
      return "Error"

# Define the eval_expression function

def eval_expression(user_input: str, ) -> str:

    '''
  This function takes the user input, uses the  Python's eval() function to evaluate the exression and return it.

  Args:
      user_input (str): The user input string.

  Returns:
      str: The solution to the expression.

  '''


    try:
        
        result = eval(user_input, {"__builtins__": None, "math": math, "PI": math.pi})
        return f" {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception:
        return "Error: Invalid mathematical expression. Please try again."

# Define the add function
def add(a: float, b: float) -> str:
    '''
    Adds two numbers.
    Args:
      a (float): a floating point number
      b (float): a floating point number
    Returns:
      float: The sum of a and b
    '''
    a = float(a)
    b = float(b)
    return f"{a + b}"

# Define the subtract function
def subtract(a: float, b: float) -> str:
    '''Subtracts one number from another.
       Args:
      a (float): a floating point number
      b (float): a floating point number
    Returns:
      float: The difference between a and b
    '''
    a = float(a)
    b = float(b)
    return f"{a - b}"

# Define the multiply function
def multiply(a: float, b: float) -> str:
    '''Multiplies two numbers.
        Args:
          a (float): a floating point number
          b (float): a floating point number
        Returns:
          float: The product of a and b
'''

    a = float(a)
    b = float(b)
    return f"{a * b}"

# Define the divide function
def divide(a: float, b: float) -> str:
    '''Divides one number by another. Raises an error if b is zero.
        Args:
          a (float): a floating point number
          b (float): a floating point number
        Returns:
         float: The quotient of b divided by a

'''
    a = float(a)
    b = float(b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return f"{a / b}"


# Define the percentage function
def percentage(a: float, b: float) -> str:
    '''Calculates a as a percentage of b.
Args:
      a (float): a floating point number
      b (float): a floating point number
    Returns:
      float: a as a percentage of b

'''


    a = float(a)
    b = float(b)
    if b == 0:
        raise ZeroDivisionError("Cannot calculate percentage of zero.")
    return f"{ (a / b) * 100}"

# Define the sine function

def sine(x: float) -> str:
    '''Calculates the sine of an angle (in radians).

Args:
      x (float): a floating point number

    Returns:
      float: the sine of an angle (in radians)
'''
    x = float(x)
    return f"{math.sin(x)}"

# Define the cosine function
def cosine(x: float) -> str:
    '''Calculates the cosine of an angle (in radians).


Args:
     x (float): a floating point number

    Returns:
      float: the cosine of an angle (in radians)
''' 
    x = float(x)
    return f"{math.cos(x)}"

# Define the tangent function
def tangent(x: float) -> str:
    '''Calculates the tangent of an angle (in radians).
Args:
      x (float): a floating point number

    Returns:
      float: the tangent of an angle (in radians)

'''
    x = float(x)
    return f"{math.tan(x)}"

# Define the square_root function
def square_root(x: float) -> str:
    '''Calculates the square root of a number.

Args:
      x (float): a floating point number

    Returns:
      float: the square root of a number

'''
    x = float(x)
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return f"{math.sqrt(x)}"

# Define the logarithm function
def logarithm(x: float, base:float=10) -> str:
    '''Calculates the logarithm of a number with a given base (default base 10).

Args:
      x (float): a floating point number

    Returns:
      float: the logarithm of a number with a base 10

'''
    x = float(x)
    if x <= 0:
        raise ValueError("Cannot calculate the logarithm of a non-positive number.")
    return f"{math.log(x, base)}"


# Create the tools object for LLM's evaluation

tools = [
    Tool(
        name="get_expression_type",
        func=get_expression_type,
        description="Use this tool to determine the type of expression.",
    ),
    Tool(
        name="eval_expression",
        func=eval_expression,
        description="Use this tool to evaluate the expression.",
    ),
    Tool(
        name="add",
        func=add,
        description="Use this tool to add two numbers.",
    ),
    Tool(
        name="subtract",
        func=subtract,
        description="Use this tool to subtract one number from another.",
    ),
    Tool(
        name="multiply",
        func=multiply,
        description="Use this tool to multiply two numbers.",
    ),
    Tool(
        name="divide",
        func=divide,
        description="Use this tool to divide one number by another.",
    ),
    Tool(            
        name="percentage",
        func=percentage,
        description="Use this tool to calculate a as a percentage of b.",
    ),
    Tool(
        name="sine",
        func=sine,
        description="Use this tool to calculate the sine of an angle (in radians).",
    ),
    Tool(
        name="cosine",
        func=cosine,
        description="Use this tool to calculate the cosine of an angle (in radians).",
    ),
    Tool(
        name="tangent",
        func=tangent,
        description="Use this tool to calculate the tangent of an angle (in radians).",
    ),
    Tool(
        name="square_root",
        func=square_root,
        description="Use this tool to calculate the square root of a number.",
    ),
    Tool(
        name="logarithm",
        func=logarithm,
        description="Use this tool to calculate the logarithm of a number.",
    )
]

# Initialize the agent

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# User interaction loop
print("Welcome to the Expression Evaluator! Type 'exit' to quit.")
while True:
    print("Entering sleep")
    time.sleep(66)
    user_input = input("\nEnter a mathematical expression (e.g., '5 + 3', '50 / 2'): ").strip()
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    else:
        #response = agent.run(user_input)
        response = agent.run({"input": user_input})

        print(f"\nResult: {response}")
