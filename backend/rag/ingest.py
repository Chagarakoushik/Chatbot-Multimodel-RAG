from backend.rag.chroma_db import add_to_db,clear_db
from backend.models.vision import extract_text_from_image
from pypdf import PdfReader


def chunk_text(text, chunk_size=500, overlap=100):
    clear_db()
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def ingest_pdf(file):
    reader = PdfReader(file)
    clear_db()
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    chunks = chunk_text(text)
    add_to_db(chunks)

    return "PDF ingested successfully"


def ingest_image(image_bytes):
    clear_db()
    text = extract_text_from_image(image_bytes)

    chunks = chunk_text(text)
    add_to_db(chunks)

    return "Image processed & stored successfully"