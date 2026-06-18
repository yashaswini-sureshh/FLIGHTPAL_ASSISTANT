from src.rag.document_loader import load_documents
from src.rag.text_processing import create_chunks
from src.rag.vector_store import build_vector_store

DATA_FOLDER = "./data"

documents = load_documents(DATA_FOLDER)

chunks = create_chunks(documents)

build_vector_store(chunks)

print("Database Created Successfully")