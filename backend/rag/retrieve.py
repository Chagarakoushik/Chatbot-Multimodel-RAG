from backend.rag.chroma_db import query_db

def retrieve(query):
    docs = query_db(query)
    return " ".join(docs)