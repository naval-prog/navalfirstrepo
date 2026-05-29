from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

def retrieve_docs(query, k=2):
    docs = db.similarity_search(query, k=k)

    results = []

    for i, doc in enumerate(docs):
        results.append({
            "content": doc.page_content,
            "source": doc.metadata.get("source"),
            "chunk": i
        })

    return results