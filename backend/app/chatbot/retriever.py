from langchain_chroma import Chroma

from app.chatbot.embeddings import create_embeddings


def get_retriever():
    _, embeddings = create_embeddings()

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever