# Later, load the index
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
import asyncio
import os
import index


# Build index
query_engine = index.build()

# Load index
# query_engine = index.load()

# Tools
async def search_documents(query: str) -> str:
    """This contains the job descriptions, CVs and cover letters."""
    response = await query_engine.aquery(query)
    print("Searched documents which is computationally expensive")
    return str(response)

# Create an agent
agent = FunctionAgent(
    tools=[search_documents],
    llm=OpenAI(model="gpt-4o-mini"),
    system_prompt="""You are a helpful assistant to increase the success of people getting jobs.""",
)

async def main():
    # Run the agent
    response = await agent.run("In what ways is Jane Doe qualified to be an apple eater?")
    print(str(response))

# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
