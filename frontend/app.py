import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("🧠 Multimodal RAG Chatbot")

# -----------------------
# Sidebar
# -----------------------
st.sidebar.header("Upload Data")

pdf_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])
if pdf_file:
    try:
        files = {"file": pdf_file}
        res = requests.post(f"{BACKEND_URL}/upload/pdf", files=files)
        st.sidebar.success(res.json().get("message", "Uploaded"))
    except:
        st.sidebar.error("❌ Backend not running")

image_file = st.sidebar.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
if image_file:
    try:
        files = {"file": image_file}
        res = requests.post(f"{BACKEND_URL}/upload/image", files=files)
        st.sidebar.success(res.json().get("message", "Uploaded"))
    except:
        st.sidebar.error("❌ Backend not running")

st.sidebar.subheader("⚙️ Controls")

if st.sidebar.button("🗑️ Clear Data"):
    try:
        res = requests.post(f"{BACKEND_URL}/clear")
        st.session_state.clear()
        st.sidebar.success(res.json().get("message", "Cleared"))
    except:
        st.sidebar.error("❌ Backend not running")

# -----------------------
# Chat Section
# -----------------------
st.subheader("💬 Ask Questions")

query = st.text_input("Enter your question")

if st.button("Ask"):
    if not query:
        st.warning("Please enter a question.")
    else:
        try:
            res = requests.post(
                f"{BACKEND_URL}/chat",
                params={"query": query}
            )

            if res.status_code == 200:
                data = res.json()
                st.success(data.get("response", "No response"))
            else:
                st.error("Backend error")

        except Exception as e:
            st.error("❌ Backend not running")