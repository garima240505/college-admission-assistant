from langchain_huggingface import HuggingFaceEmbeddings

from app.chatbot.loader import load_documents
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_embeddings():
    # Load PDF
    documents = load_documents()

    # Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    # Create embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    return chunks, embeddings