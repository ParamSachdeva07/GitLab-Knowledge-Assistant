from src.db.client import client, collection
from fastembed import SparseTextEmbedding
from openai import OpenAI
from qdrant_client import models


def top_k_semantic(query, k = 20, collection = collection, client = client):
    with OpenAI() as embedding_client:
        res = embedding_client.embeddings.create(
            input=query, 
            model="text-embedding-3-small"
            )
        
    hits = client.query_points(
        collection_name=collection, 
        query=res.data[0].embedding,
        using='dense',
        limit=k
        ).points
    return hits

bm25 = SparseTextEmbedding(model_name='Qdrant/bm25')

def top_k_bm25(query, k=20, collection=collection, client=client):
    query_vector = list(bm25.query_embed(query))[0]

    hits = client.query_points(
        collection_name=collection,
        query=models.SparseVector(
            indices=query_vector.indices.tolist(),
            values=query_vector.values.tolist(),
        ),
        using="bm25",
        limit=k,
    ).points

    return hits

def reciprocal_rank_fusion(semantic_hits, bm25_hits, limit=10, constant=60):
    combined = {}

    for hits in (semantic_hits, bm25_hits):
        for rank, hit in enumerate(hits, start=1):
            if hit.id not in combined:
                combined[hit.id] = {
                    "id": hit.id,
                    "payload": hit.payload,
                    "rrf_score": 0.0,
                }

            combined[hit.id]["rrf_score"] += 1 / (constant + rank)

    ranked = sorted(
        combined.values(),
        key=lambda item: item["rrf_score"],
        reverse=True,
    )

    return ranked[:limit]

def retrieve(query, k = 10):
    semantic_hits = top_k_semantic(query, k = 2 * k)
    bm25_hits = top_k_bm25(query, k = 2 * k)

    reranked = reciprocal_rank_fusion(
        semantic_hits=semantic_hits, 
        bm25_hits=bm25_hits, 
        limit = 2 * k
        )
    return reranked

'''hits = top_k_bm25('What is GitLab’s parental leave policy, and who is eligible?', k = 1)

for hit in hits:
    print(hit.score)
    print(hit.payload['page_content'])
    print(hit.payload['metadata'])'''



