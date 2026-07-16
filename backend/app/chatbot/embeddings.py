from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

from app.chatbot.loader import load_documents


def create_embeddings():
    # Load PDF
    documents = load_documents()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    # Create embedding model
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    return chunks, embeddings