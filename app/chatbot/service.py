from app.chatbot.chain import create_chain


def get_chat_response(question: str):
    llm, retriever = create_chain()

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Combine retrieved context
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an AI Admission Assistant.

Answer ONLY using the information provided in the context below.

If the answer is not present in the context, reply:
"I couldn't find that information in the admission documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content