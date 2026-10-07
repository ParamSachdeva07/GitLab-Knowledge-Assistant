from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownTextSplitter
import frontmatter

data_path = '../../data/cleaned/content'

loader = DirectoryLoader(data_path, glob="**/*.md", loader_cls=TextLoader, recursive=True, loader_kwargs={"encoding": "utf-8"},)

documents = loader.load()

for document in documents:
    yaml_metadata, content = frontmatter.parse(document.page_content)
    document.page_content = content
    document.metadata = {
        **document.metadata,
        **yaml_metadata
    }

splitter = MarkdownTextSplitter()

chunks = splitter.split_documents(documents)
