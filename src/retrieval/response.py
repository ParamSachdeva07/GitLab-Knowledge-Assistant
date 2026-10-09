import os
from openai import OpenAI

from src.retrieval.top_k_chunks import retrieve
from src.retrieval.reranker import rerank
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def getResponse(query, k = 10):
    candidates = retrieve(query, k=20)
    chunks = rerank(query, candidates, k=k)

    context = "\n\n".join(
        f"[s{index + 1}]\n{chunk['payload']['page_content']}\n {chunk['payload']['metadata']}" for index, chunk in enumerate(chunks)
    )
    response = client.responses.create(
        model="gpt-5.5",
        reasoning={"effort": "none"},
        instructions="You are an enterprise knowledge assistant. you will provided information on what to respond to query with. Cite sources as provided for example [S1], [S2] Capital S only, do not cite unmentioned sources",
        input=query + context,
    )

    return {
        'response' : response.output_text,
        'chunks': chunks
            }
