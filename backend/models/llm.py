import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context, query):
    print(client.models.list())
    prompt = f"""
    You are a helpful assistant.

    Answer the question using ONLY the context below.
    If the answer is incomplete, explain clearly.

    Context:
    {context}

    Question:
    {query}

    Give a detailed answer If you can't answer tell to use websearch api.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # ✅ WORKING MODEL
        messages=[
            {"role": "system", "content": "Answer based on context only."},
            {"role": "user", "content": prompt}
        ]
    )


    return response.choices[0].message.content