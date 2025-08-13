from SimpleCodeExecutor import SimpleCodeExecutor
from llama_index.llms.openai import OpenAI
import asyncio

# Define a few helper functions
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return a / b

# Setup the agent
code_executor = SimpleCodeExecutor(
    # give access to our functions defined above
    locals={
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    },
    globals={
        # give access to all builtins
        "__builtins__": __builtins__,
        # give access to numpy
        "np": __import__("numpy"),
    },
)

# Use the agent
from llama_index.core.agent.workflow import CodeActAgent
from llama_index.core.workflow import Context

agent = CodeActAgent(
    code_execute_fn=code_executor.execute,
    llm=OpenAI(model="gpt-4o-mini"),
    tools=[add, subtract, multiply, divide],
)

# context to hold the agent's session/state/chat history
ctx = Context(agent)

from llama_index.core.agent.workflow import (
    ToolCall,
    ToolCallResult,
    AgentStream,
)


async def run_agent_verbose(agent, ctx, query):
    handler = agent.run(query, ctx=ctx)
    print(f"User:  {query}")
    async for event in handler.stream_events():
        if isinstance(event, ToolCallResult):
            print(
                f"\n-----------\nCode execution result:\n{event.tool_output}"
            )
        elif isinstance(event, ToolCall):
            print(f"\n-----------\nParsed code:\n{event.tool_kwargs['code']}")
        elif isinstance(event, AgentStream):
            print(f"{event.delta}", end="", flush=True)

    return await handler

async def main():
    response = await run_agent_verbose(
        agent, ctx, "Calculate the sum of all numbers from 1 to 10"
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())