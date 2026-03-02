from fastapi import FastAPI, UploadFile, File
from backend.rag.retrieve import retrieve
from backend.models.llm import generate_answer
from backend.rag.ingest import ingest_pdf, ingest_image
from backend.rag.chroma_db import clear_db

app = FastAPI()

from backend.tools.router import decide_tool
from backend.tools.web_search import web_search

@app.post("/chat")
async def chat(query: str):

    tool = decide_tool(query)

    # 🔥 WEB SEARCH
    if tool == "web_search":
        result = web_search(query)
        return {"response": result}

    # 🔥 RAG (default)
    context = retrieve(query)
    answer = generate_answer(context, query)
    return {"response": answer}


@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    result = ingest_image(content)
    return {"message": result}


@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    result = ingest_pdf(file.file)
    return {"message": result}

@app.post("/clear")
async def clear():
    clear_db()
    return {"message": "Database cleared"}