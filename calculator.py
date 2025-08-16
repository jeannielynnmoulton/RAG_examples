import asyncio
import os
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

# Set OpenAI key
# Done in ~/.zshrc

# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b

# Define a simple calculator tool
def add(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a + b


# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    tools=[multiply],
    llm=OpenAI(model="gpt-4o-mini"),
    system_prompt="You are a helpful assistant that can multiply or add two numbers. You need to interpret the expression they enter.",
)


async def main():
    # Run the agent
    response = await agent.run("What is 1234 + 4567?")
    print(str(response))


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
