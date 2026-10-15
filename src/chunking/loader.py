from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownTextSplitter
import frontmatter
from src.db.client import client, collection
import json
from uuid import uuid5, NAMESPACE_URL
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
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

def chunk_ids(chunks, repo_root=None):
    """Stable IDs for source, content and location; preserve repeated chunks."""
    repo_root = repo_root or Path(__file__).resolve().parents[2] / "data" / "handbook"
    occurrences = defaultdict(int)
    ids = []
    for chunk in chunks:
        source = Path(chunk.metadata["source"]).resolve().relative_to(repo_root.resolve()).as_posix()
        identity = json.dumps({
            "repository": "gitlab-handbook",
            "source": source,
            "content": chunk.page_content,
            "location": {key: chunk.metadata[key] for key in
                         ("page_number", "sheet", "row_start", "row_end")
                         if key in chunk.metadata},
        }, sort_keys=True, ensure_ascii=False)
        occurrence = occurrences[identity]
        occurrences[identity] += 1
        ids.append(str(uuid5(NAMESPACE_URL, json.dumps([identity, occurrence]))))
    return ids


@lru_cache(maxsize=1)
def get_bm25_model():
    return SparseTextEmbedding(model_name="Qdrant/bm25")


def add_chunks(chunks, collection = collection, batch_size=100):
    if batch_size < 1:
        raise ValueError("batch_size must be greater than zero")

    ids = chunk_ids(chunks)
    bm25 = get_bm25_model()
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
                    id=chunk_id,
                    vector={
                        "dense": dense.embedding,
                        "bm25": models.SparseVector(
                            indices=sparse.indices.tolist(), values=sparse.values.tolist(),
                        ),
                    },
                    payload={"page_content": chunk.page_content, "metadata": chunk.metadata},
                )
                for chunk_id, chunk, dense, sparse in zip(
                    ids[start:start + batch_size], batch, dense_vectors, sparse_vectors, strict=True,
                )
            ]
            client.upsert(collection_name=collection, points=points, wait=True)

    return {"input_tokens": total_input_tokens, "chunks_added": len(chunks)}


if __name__ == "__main__":
    chunks = load_directory()
    add_chunks(chunks, collection)
