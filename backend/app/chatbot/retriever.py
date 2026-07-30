from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    return retriever