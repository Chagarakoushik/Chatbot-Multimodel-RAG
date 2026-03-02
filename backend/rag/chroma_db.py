import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection("rag_db")

model = SentenceTransformer("all-MiniLM-L6-v2")

def add_to_db(texts):
    embeddings = model.encode(texts).tolist()
    ids = [str(i) for i in range(len(texts))]

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=ids
    )

def query_db(query):
    query_embedding = model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=6)

    if not results["documents"]:
        return []

    return results["documents"][0]

def clear_db():
    global collection
    client.delete_collection("rag_db")
    collection = client.create_collection("rag_db")