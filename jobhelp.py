from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
import asyncio
import os

# Set OPENAI_API_KEY env variable
# Done in ~/.zshrc

# Create a RAG tool using LlamaIndex
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Tools
async def search_documents(query: str) -> str:
    """This contains the job descriptions, CVs and cover letters."""
    response = await query_engine.aquery(query)
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
