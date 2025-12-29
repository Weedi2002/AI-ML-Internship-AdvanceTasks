import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

st.set_page_config(page_title="Context-Aware RAG Chatbot")

st.title("📘 Context-Aware Chatbot (Gemini + RAG)")

# Load vectorstore
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = FAISS.load_local("faiss_index", embeddings)

# Initialize session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
query = st.text_input("Ask a question:")

if query:
    response = qa_chain({
        "question": query,
        "chat_history": st.session_state.chat_history
    })

    st.session_state.chat_history.append((query, response["answer"]))

    st.markdown("### Answer")
    st.write(response["answer"])

    st.markdown("### Conversation History")
    for q, a in st.session_state.chat_history:
        st.write(f"**Q:** {q}")
        st.write(f"**A:** {a}")
