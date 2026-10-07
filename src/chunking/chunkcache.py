import json
from pathlib import Path
from langchain_core.documents import Document

def cache_chunks(chunks):
    cache_path = Path('../../data/chunks.jsonl')
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    with cache_path.open('w', encoding="utf-8") as file:
        for chunk in chunks:
            record = {
                "page_content": chunk.page_content,
                "metadata": chunk.metadata
            }
            json_data = json.dumps(record, ensure_ascii=False, default=str) + "\n"
            file.write(json_data)

def retrieve_chunks(path):
    with path.open('r', encoding='utf-8') as file:
        chunks = [Document(**json.loads(line)) for line in file if line.strip()]