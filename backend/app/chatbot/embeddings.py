from langchain_huggingface import HuggingFaceEmbeddings
from app.chatbot.loader import load_documents
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_embeddings():
    # Load PDF documents
    documents = load_documents()

    # Split into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    # Lightweight embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    return chunks, embeddings