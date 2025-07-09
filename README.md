# 💬 RAG Chatbot — AI Assistant Powered by LangChain, FAISS, and Streamlit

[![🚀 Live Demo](https://img.shields.io/badge/%F0%9F%9A%80%20Live%20Demo-Streamlit-brightgreen?style=for-the-badge)](https://rag-chatbot-jb.streamlit.app/)

---

## 📌 Overview

This is a **Retrieval-Augmented Generation (RAG)** based chatbot built using:

- **LangChain** for chaining components (retriever + LLM)
- **FAISS** for semantic vector search
- **Sentence Transformers** for high-quality embeddings
- **Streamlit** for a simple, clean web UI
- **OpenAI GPT-3.5** as the LLM backend

It reads your documents (PDF, DOCX, TXT), indexes them, and answers your questions using the most relevant chunks — with proper source citations.

---

## 🧠 What This Project Does

✔️ Ingests documents from the `data/` folder  
✔️ Splits them into semantic chunks  
✔️ Embeds them using `multi-qa-MiniLM-L6-cos-v1`  
✔️ Stores vectors in FAISS index  
✔️ Uses LangChain RAG pipeline to answer questions  
✔️ Displays source file citations  
✔️ Rebuilds the FAISS index automatically if missing  
✔️ Web interface powered by Streamlit  
✔️ Feedback buttons included (👍 / 👎)

---

## ⚙️ Tech Stack

| Component        | Technology                        |
|------------------|-----------------------------------|
| 🔄 RAG Pipeline  | `LangChain`                       |
| 🔎 Vector DB     | `FAISS`                           |
| 🧠 Embeddings     | `Sentence-Transformers` (multi-qa-MiniLM-L6-cos-v1) |
| 🤖 LLM           | `OpenAI GPT-3.5 Turbo`            |
| 📄 Document Load | `PyMuPDF`, `docx2txt`, `TextLoader` |
| 🌐 Web UI        | `Streamlit`                       |
| 🔐 Secrets Mgmt  | `.env` with `python-dotenv`       |

---

## 🧪 Example Questions

- What is LangChain?
- What are the core concepts of Transformers?
- What is polymorphism in Python?
- Summarize OpenAI's features

---

## 🚀 How to Run Locally

### 🔧 1. Clone the repo

```bash
git clone https://github.com/JalajBaghwala/rag-chatbot.git
cd rag-chatbot
