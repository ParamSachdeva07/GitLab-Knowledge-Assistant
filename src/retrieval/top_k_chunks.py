from src.db.client import client, collection
from fastembed import SparseTextEmbedding
from fastembed.rerank.cross_encoder import TextCrossEncoder
from openai import OpenAI
from qdrant_client import models
from time import perf_counter
from langfuse import observe

embedding_client = OpenAI()

@observe(name="semantic_search", capture_input=False, capture_output=False)
def top_k_semantic(query, k = 20, collection = collection, client = client):
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

@observe(name="bm25_search", capture_input=False, capture_output=False)
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

@observe(name="rrf", capture_input=False, capture_output=False)
def reciprocal_rank_fusion(semantic_hits, bm25_hits, limit=10, constant=60):
    combined = {}

    for method, hits in (
        ("semantic", semantic_hits),
        ("bm25", bm25_hits),
    ):
        for rank, hit in enumerate(hits, start=1):
            if hit.id not in combined:
                combined[hit.id] = {
                    "id": hit.id,
                    "payload": hit.payload,
                    "semantic_score": None,
                    "semantic_rank": None,
                    "bm25_score": None,
                    "bm25_rank": None,
                    "rrf_score": 0.0,
                }

            combined[hit.id][f"{method}_score"] = hit.score
            combined[hit.id][f"{method}_rank"] = rank
            combined[hit.id]["rrf_score"] += 1 / (constant + rank)

    ranked = sorted(
        combined.values(),
        key=lambda item: item["rrf_score"],
        reverse=True,
    )

    return ranked[:limit]

reranker = TextCrossEncoder(
    model_name="Xenova/ms-marco-MiniLM-L-6-v2",
)



@observe(name="reranking", capture_input=False, capture_output=False)
def rerank(query, chunks, k=5):
    if not chunks:
        return []

    documents = [
        chunk["payload"]["page_content"]
        for chunk in chunks
    ]
    scores = list(reranker.rerank(query, documents, batch_size=8))

    scored_chunks = [
        {
            **chunk,
            "rrf_rank": rank,
            "cross_encoder_score": float(score),
        }
        for rank, (chunk, score) in enumerate(
            zip(chunks, scores, strict=True), start=1
        )
    ]

    return sorted(
        scored_chunks,
        key=lambda chunk: chunk["cross_encoder_score"],
        reverse=True,
    )[:k]


@observe(name='retrieval', capture_output=False)
def retrieve(query, k=5, candidate_k=8):
    t0 = perf_counter()
    semantic_hits = top_k_semantic(query, k=2 * candidate_k)
    t1 = perf_counter()
    bm25_hits = top_k_bm25(query, k=2 * candidate_k)
    t2 = perf_counter()

    candidates = reciprocal_rank_fusion(
        semantic_hits=semantic_hits,
        bm25_hits=bm25_hits,
        limit=candidate_k,
    )
    t3 = perf_counter()
    chunks = rerank(query, candidates, k=k)
    t4 = perf_counter()

    return {
        "chunks": chunks,
        "timings_ms": {
            "semantic": (t1 - t0) * 1000,
            "bm25": (t2 - t1) * 1000,
            "rrf": (t3 - t2) * 1000,
            "reranking": (t4 - t3) * 1000,
            "retrieval_total": (t4 - t0) * 1000,
        },
    }

'''hits = top_k_bm25('What is GitLab’s parental leave policy, and who is eligible?', k = 1)

for hit in hits:
    print(hit.score)
    print(hit.payload['page_content'])
    print(hit.payload['metadata'])'''
