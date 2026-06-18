from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_chroma import Chroma


def build_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./database/flight_db"
    )

    return db


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="./database/flight_db",
        embedding_function=embeddings
    )

    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever