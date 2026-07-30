from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


def create_chain(llm, retriever):

    prompt = ChatPromptTemplate.from_template(
        """
        You are AIT Admission Assistant.

        Answer the question only using the provided context.

        If the answer is not available in the context,
        say:
        "I could not find this information in the admission documents."

        Context:
        {context}

        Question:
        {input}
        """
    )


    def format_docs(docs):
        return "\n\n".join(
            doc.page_content for doc in docs
        )


    rag_chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
    )


    return rag_chain