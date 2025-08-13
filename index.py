from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def build():
    """Builds an index from the documents in data directory, makes it persistent and returns the query index"""
    # Create a RAG tool using LlamaIndex
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    # Persistent storage
    index.storage_context.persist("storage")
    return query_engine

def load():
    """Loads index from storage directory and returns the query engine"""
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    return query_engine