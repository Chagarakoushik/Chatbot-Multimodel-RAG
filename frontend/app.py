import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("🧠 Multimodal RAG Chatbot")

# Sidebar
st.sidebar.header("Upload Data")

pdf_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])
if pdf_file:
    files = {"file": pdf_file}
    res = requests.post("http://127.0.0.1:8000/upload/pdf", files=files)
    st.sidebar.success(res.json()["message"])

image_file = st.sidebar.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
if image_file:
    files = {"file": image_file}
    res = requests.post("http://127.0.0.1:8000/upload/image", files=files)
    st.sidebar.success(res.json()["message"])
st.sidebar.subheader("⚙️ Controls")

if st.sidebar.button("🗑️ Clear Data"):
    res = requests.post("http://127.0.0.1:8000/clear")
    st.session_state.clear()
    st.sidebar.success(res.json()["message"])
# Chat
st.subheader("💬 Ask Questions")

query = st.text_input("Enter your question")

if st.button("Ask"):
    try:
        res = requests.post(
            "http://127.0.0.1:8000/chat",
            params={"query": query}
        )

        # st.write("Status:", res.status_code)
        # st.write("Raw response:", res.text)

        if res.status_code == 200:
            data = res.json()
            st.success(data.get("response", "No response"))
        else:
            st.error("Backend error")

    except Exception as e:
        st.error(f"Error: {e}")