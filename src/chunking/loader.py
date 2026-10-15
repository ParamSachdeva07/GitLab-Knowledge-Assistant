from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownTextSplitter
import frontmatter
from src.chunking.chunkcache import cache_chunks
from src.db.client import client, collection
import json
from uuid import uuid4
from openai import OpenAI
from fastembed import SparseTextEmbedding
from qdrant_client import models
from langchain_core.documents import Document


def normalize_metadata(metadata):
    return json.loads(json.dumps(metadata, ensure_ascii=False, default=str))

#inital chunking process
def load_directory(data_path = '../../data/handbook'):

    loader = DirectoryLoader(data_path, glob="**/*.md", loader_cls=TextLoader, recursive=True, loader_kwargs={"encoding": "utf-8"},)

    documents = loader.load()

    for document in documents:
        yaml_metadata, content = frontmatter.parse(document.page_content)

        document.page_content = content
        document.metadata = {
            **document.metadata,
            **normalize_metadata(yaml_metadata),
            "source": document.metadata["source"],
        }

    splitter = MarkdownTextSplitter()

    chunks = splitter.split_documents(documents)
    return chunks

#cache_chunks(chunks)

def add_chunks(chunks, collection = collection, batch_size=100):
    if batch_size < 1:
        raise ValueError("batch_size must be greater than zero")

    bm25 = SparseTextEmbedding(model_name="Qdrant/bm25")
    total_input_tokens = 0
    with OpenAI() as embedding_client:
        for start in range(0, len(chunks), batch_size):
            batch = chunks[start:start + batch_size]
            texts = [chunk.page_content for chunk in batch]

            response = embedding_client.embeddings.create(
                model="text-embedding-3-small", input=texts,
            )
            total_input_tokens += response.usage.prompt_tokens


            dense_vectors = sorted(response.data, key=lambda item: item.index)
            sparse_vectors = list(bm25.embed(texts))

            points = [
                models.PointStruct(
                    id=str(uuid4()),
                    vector={
                        "dense": dense.embedding,
                        "bm25": models.SparseVector(
                            indices=sparse.indices.tolist(), values=sparse.values.tolist(),
                        ),
                    },
                    payload={"page_content": chunk.page_content, "metadata": chunk.metadata},
                )
                for chunk, dense, sparse in zip(batch, dense_vectors, sparse_vectors, strict=True)
            ]
            client.upsert(collection_name=collection, points=points, wait=True)

    return {"input_tokens": total_input_tokens, "chunks_added": len(chunks)}


if __name__ == "__main__":
    chunks = load_directory()
    add_chunks(chunks, collection)
