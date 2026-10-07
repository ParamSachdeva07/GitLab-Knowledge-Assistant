from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownTextSplitter
import frontmatter
from chunkcache import cache_chunks
from src.db.client import collection
import json
from flatten_json import flatten

def flatten_metadata(metadata):
    normalised = json.loads(
        json.dumps(metadata, ensure_ascii=False, default=str)
        )
    flattened = flatten(normalised)
    metadata = {**flattened}
    return metadata


def load_documents(data_path = '../../data/cleaned/content'):

    loader = DirectoryLoader(data_path, glob="**/*.md", loader_cls=TextLoader, recursive=True, loader_kwargs={"encoding": "utf-8"},)

    documents = loader.load()

    for document in documents:
        yaml_metadata, content = frontmatter.parse(document.page_content)
            
        document.page_content = content
        document.metadata = {
            **document.metadata,
            **flatten_metadata(yaml_metadata)
        }

    splitter = MarkdownTextSplitter()

    chunks = splitter.split_documents(documents)
    return chunks

chunks = load_documents()
cache_chunks(chunks)




