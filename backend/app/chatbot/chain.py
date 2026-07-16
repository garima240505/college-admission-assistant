from langchain_ollama import ChatOllama

from app.chatbot.retriever import get_retriever


def create_chain():
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    retriever = get_retriever()

    return llm, retriever