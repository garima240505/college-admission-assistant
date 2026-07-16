from langchain_chroma import Chroma

from app.chatbot.embeddings import create_embeddings


def create_vectorstore():
    chunks, embeddings = create_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vectorstore