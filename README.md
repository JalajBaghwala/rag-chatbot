# RAG Chatbot using LangChain + FAISS + Streamlit

## 🔍 Overview

This is a Retrieval-Augmented Generation (RAG) based chatbot that:
- Ingests multiple document formats (PDF, DOCX, TXT)
- Converts them into vector embeddings (Sentence Transformers)
- Stores them in FAISS
- Answers queries with GPT-3.5 using the retrieved content
- Includes source citations
- Offers a Streamlit UI for interaction

---

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/JalajBaghwala/rag-chatbot.git
cd rag-chatbot
