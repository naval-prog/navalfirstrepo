import chromadb
from sentence_transformers import SentenceTransformer

document=[
  "Python is a popular programming language for AI and web development.",
    "RAG combines retrieval and generation to improve LLM responses.",
    "ChromaDB is a vector database used for storing embeddings."
]

ids = ["doc1", "doc2", "doc3"]

model=SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(document).tolist()


client = chromadb.Client()

collection = client.get_or_create_collection(
    name="demo_collection"
)

collection.add(
    ids=ids,
    documents=document,
    embeddings=embeddings
)

query_embedding = model.encode("How does RAG help language models?").tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print("Query:", "How does RAG help language models?")
print("\nTop 2 Results:")

for doc in results["documents"][0]:
    print("-", doc)
