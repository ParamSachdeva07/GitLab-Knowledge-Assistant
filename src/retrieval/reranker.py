from fastembed.rerank.cross_encoder import TextCrossEncoder


reranker = TextCrossEncoder(
    model_name="Xenova/ms-marco-MiniLM-L-6-v2",
)


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
