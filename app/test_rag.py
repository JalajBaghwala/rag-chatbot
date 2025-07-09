from rag_engine import run_rag_query

if __name__ == "__main__":
    query = input("Enter your question: ")
    answer, citations = run_rag_query(query)

    print("\n📌 Answer:\n", answer)
    print("\n📄 Sources:", list(citations))
