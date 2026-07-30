from langchain_groq import ChatGroq

from app.config import settings
from app.chatbot.retriever import get_retriever
from app.chatbot.chain import create_chain


# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=settings.GROQ_API_KEY
)


retriever = get_retriever()


qa_chain = create_chain(
    llm=llm,
    retriever=retriever
)


def get_chat_response(question: str):

    try:
        response = qa_chain.invoke(question)

        return response.content

    except Exception as e:
        print("CHATBOT ERROR:", e)
        return "Sorry, I am unable to process your request right now."