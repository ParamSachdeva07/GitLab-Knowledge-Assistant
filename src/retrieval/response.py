from dotenv import load_dotenv

load_dotenv()

from langfuse import observe
from langfuse.openai import openai  # pyright: ignore[reportPrivateImportUsage]
from src.retrieval.top_k_chunks import retrieve


client = openai.OpenAI()

@observe(name="answer")
def getResponse(query, k = 5):
    retrieval = retrieve(query, k=k)
    chunks = retrieval["chunks"]

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
        'chunks': chunks,
        'timings_ms': retrieval["timings_ms"],
            }
