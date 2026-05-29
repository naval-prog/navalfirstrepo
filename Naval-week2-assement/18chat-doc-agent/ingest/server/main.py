from agent.graph import graph

while True:

    q = input("You: ")

    if q == "exit":
        break

    result = graph.invoke(
        {
            "question": q,
            "retrieved_docs": [],
            "answer": "",
            "use_retrieval": False
        }
    )

    print(result["answer"])