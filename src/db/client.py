from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

load_dotenv()

client = QdrantClient(url="http://localhost:6333")
collection = "gitlab_docs_v1"

if not client.collection_exists(collection):
    client.create_collection(
        collection_name=collection,
        vectors_config={
            "dense": models.VectorParams(size=1536, distance=models.Distance.COSINE),
        },
        sparse_vectors_config={
            "bm25": models.SparseVectorParams(modifier=models.Modifier.IDF),
        },
    )
