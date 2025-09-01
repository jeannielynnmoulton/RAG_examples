import dotenv
from llama_index.core import PromptTemplate, TreeIndex
from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from rich.console import Console
from rich.markdown import Markdown

def main():
    # set open AI key
    dotenv.load_dotenv()

    # Set up LLM
    llm = OpenAI(model="gpt-3.5-turbo")

    ### We're going to create a tool that help summarize what LlamaIndex does in a top down fashion
    ### and ask the tool to write short summaries to help me explore more of LlamaIndex in a
    ### time-efficient way

    # Use a web reader to ingest data (handselecting to avoid using web crawler and query will be TreeIndex)
    documents = SimpleWebPageReader(html_to_text=True).load_data([
        "https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/",
        "https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/",
        "https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/"])

    # Use a TreeIndex to store summarized data
    index = TreeIndex.from_documents(documents)

    # Get users input
    user_topic = "TreeIndex"

    # Do the query and respond
    template = PromptTemplate(
        "You are required to give a summary of the topic the user has asked about if it is related to the "
        "code library LlamaIndex. If the topic is not related, then follow the rules given later. If the response"
        "is related, then do not follow those rules."
        "The aim of the summary is to teach a software engineer about the topic."
        "Start general with the topic name, a brief summary of what its purpose is."
        "Then continue to get more specific including how to use it in code and comparison to other types if applicable."
        "Format the response like a document with headings and paragraphs. "
        "Format the response in markdown."
        "The response should be concise and include class names, function names and code snippets if required."
        "The response should give concise use cases (if applicable)."
        "The response should compare the topic to other options (if applicable) in a very short bulleted list."
        "If the user asks about more than one topic, do the above iteratively for each topic. "
        "If their topic is unrelated to LlamaIndex (including just llama) follow these four rules: "
        "1) do not summarize or give any information about their topic"
        "2) state in a kind, full sentence that this is not related to LlamaIndex"
        "3) and then say a joke related to their topic"
        "4) keep all response text appropriate for work and children.\n"
        f"\n\nTopic user has asked about: {user_topic}"
    )
    query_engine = index.as_query_engine(llm=llm)
    response = query_engine.query(template.format(user_topic=user_topic))
    renderable_markup = Markdown(response.response)
    Console().print(renderable_markup)


if __name__ == "__main__":
    main()
