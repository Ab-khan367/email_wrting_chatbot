

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import pandas as pd
import os
import uuid

class Portfolio:
    def __init__(self, file_path=None):
        if file_path is None:
            file_path = os.path.join(os.path.dirname(__file__), '..', 'resource', 'my_portfolio.csv')
            file_path = os.path.abspath(file_path)

        self.data = pd.read_csv(file_path)

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore_path = os.path.join(os.path.dirname(__file__), '..', 'vectorstore')

        self.vectorstore = Chroma(
            collection_name="portfolio",
            embedding_function=self.embeddings,
            persist_directory=vectorstore_path
        )

    def load_portfolio(self):
        if self.vectorstore._collection.count() == 0:
            texts = self.data["Techstack"].tolist()
            metadatas = [{"links": l} for l in self.data["Links"]]

            self.vectorstore.add_texts(
                texts=texts,
                metadatas=metadatas
            )

    def query_links(self, skills):
        if not skills:
            return []

        if isinstance(skills, list):
            skills = " ".join(skills)

        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 2})
        docs = retriever.invoke(skills)

        # return [doc.metadata for doc in docs]
        links = [doc.metadata["links"] for doc in docs if "links" in doc.metadata]
        return links
