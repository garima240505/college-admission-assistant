from langchain_groq import ChatGroq

from app.config import settings
from app.chatbot.retriever import get_retriever
from app.chatbot.chain import create_chain


# Initialize Groq LLM (very lightweight)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=settings.GROQ_API_KEY
)


qa_chain = None


def get_qa_chain():

    global qa_chain

    if qa_chain is None:
        print("Loading retriever and chain...")

        retriever = get_retriever()

        qa_chain = create_chain(
            llm=llm,
            retriever=retriever
        )

        print("Chain loaded successfully!")

    return qa_chain


def get_chat_response(question: str):

    try:
        chain = get_qa_chain()

        response = chain.invoke(question)

        return response.content

    except Exception as e:
        print("CHATBOT ERROR:", e)

        return "Sorry, I am unable to process your request right now."