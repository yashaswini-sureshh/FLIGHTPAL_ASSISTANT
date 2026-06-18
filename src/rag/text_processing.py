import re

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    text = re.sub(
        r"[^a-zA-Z0-9.,!? ]",
        "",
        text
    )

    text = text.lower()

    return text


def create_chunks(documents):

    for doc in documents:

        doc.page_content = clean_text(
            doc.page_content
        )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(
        documents
    )

    return chunks