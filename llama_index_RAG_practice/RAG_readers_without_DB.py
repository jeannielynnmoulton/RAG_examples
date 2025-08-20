import dotenv
import nltk
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader

def install_stopwords():
    """required for SimpleWebPageReader"""
    nltk.download('stopwords')

def load_env_vars():
    """query_engine assumes OPENAI_API_KEY is in the environment, it's in the .env file"""
    dotenv.load_dotenv()

def process_data_to_query_engine():
    load_env_vars()
    # Use directory reader to read the candidate's CV and cover letter, and the job description
    documents = SimpleDirectoryReader("../data").load_data()
    # Create an index with the read documents
    index = VectorStoreIndex.from_documents(documents)
    # Convert the index to a query engine
    return index.as_query_engine()

def process_webpage_to_query_engine():
    load_env_vars()
    install_stopwords()
    documents = SimpleWebPageReader(html_to_text=True).load_data(["https://www.google.com"])
    # Create an index with the read documents
    index = VectorStoreIndex.from_documents(documents)
    # Convert the index to a query engine
    return index.as_query_engine()

def main():
    # documents
    # query_engine = process_data_to_query_engine()
    # response = query_engine.query("Tell me something about the candidate that other people might miss.")
    # print(response)

    # webpage
    query_engine = process_webpage_to_query_engine()
    response = query_engine.query("What's the first word on the google webpage?")
    print(response)

if __name__ == "__main__":
    main()
