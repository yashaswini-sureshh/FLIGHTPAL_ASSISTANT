import os
import pandas as pd

from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)


def load_documents(folder_path):

    documents = []

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        try:

            if file.endswith(".pdf"):

                loader = PyPDFLoader(file_path)

                documents.extend(loader.load())

            elif file.endswith(".txt"):

                loader = TextLoader(
                    file_path,
                    encoding="utf-8"
                )

                documents.extend(loader.load())

            elif file.endswith(".docx"):

                loader = Docx2txtLoader(file_path)

                documents.extend(loader.load())

            elif file.endswith(".xlsx"):

                excel_file = pd.ExcelFile(file_path)

                for sheet in excel_file.sheet_names:

                    df = pd.read_excel(
                        file_path,
                        sheet_name=sheet
                    )

                    documents.append(
                        Document(
                            page_content=df.to_string(index=False),
                            metadata={
                                "source": file,
                                "sheet": sheet
                            }
                        )
                    )

            print(f"Loaded: {file}")

        except Exception as e:

            print(f"Error loading {file}: {e}")

    return documents