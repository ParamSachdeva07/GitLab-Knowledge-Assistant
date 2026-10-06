from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownTextSplitter

data_path = '../../data/cleaned/content'

loader = DirectoryLoader(data_path, glob="**/*.md", loader_cls=TextLoader, recursive=True, loader_kwargs={"encoding": "utf-8"},)

documents = loader.load()

splitter = MarkdownTextSplitter()

chunks = splitter.split_documents(documents)

meta = [f"{chunk.metadata['source']}" for chunk in chunks[:10]]
print(meta)
