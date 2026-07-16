from langchain_community.document_loaders import PyPDFLoader


def load_documents():
    loader = PyPDFLoader("documents/admission.pdf")

    documents = loader.load()

    return documents