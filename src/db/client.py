import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient(path='../../data/db')

collection = client.get_or_create_collection(
    name="gitlab_docs_v1", 
    embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small")
    )
