from typing import TypedDict
from langgraph.graph import StateGraph, END
from agent import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain
)

# Shared State
class ResearchState(TypedDict):
    topic: str
    search_results: str
    scraped_content: str
    report: str
    feedback: str


# Node 1 Search
def search_node(state: ResearchState):
    search_agent = build_search_agent()

    result = search_agent.invoke({
        "messages": [
            ("user",
             f"Find recent, reliable and detailed information about {state['topic']}")
        ]
    })

    return {
        "search_results": result["messages"][-1].content
    }


# Node 2 Reader
def reader_node(state: ResearchState):
    reader_agent = build_reader_agent()

    result = reader_agent.invoke({
        "messages": [
            ("user",
             f"Based on these results pick best URL and scrape deeply:\n"
             f"{state['search_results'][:800]}")
        ]
    })

    return {
        "scraped_content": result["messages"][-1].content
    }


# Node 3 Writer
def writer_node(state: ResearchState):
    research = f"""
SEARCH RESULTS:
{state['search_results']}

SCRAPED CONTENT:
{state['scraped_content']}
"""

    report = writer_chain.invoke({
        "topic": state["topic"],
        "research": research
    })

    return {
        "report": report
    }


# Node 4 Critic
def critic_node(state: ResearchState):
    feedback = critic_chain.invoke({
        "report": state["report"]
    })

    return {
        "feedback": feedback
    }


# Build Graph
graph = StateGraph(ResearchState)

graph.add_node("search", search_node)
graph.add_node("reader", reader_node)
graph.add_node("writer", writer_node)
graph.add_node("critic", critic_node)

# Flow
graph.set_entry_point("search")
graph.add_edge("search", "reader")
graph.add_edge("reader", "writer")
graph.add_edge("writer", "critic")
graph.add_edge("critic", END)

app = graph.compile()


# Run
if __name__ == "__main__":
    topic = input("Enter topic: ")

    result = app.invoke({
        "topic": topic
    })

    print("\nSearch Results:\n", result["search_results"])
    print("\nScraped Content:\n", result["scraped_content"])
    print("\nReport:\n", result["report"])
    print("\nFeedback:\n", result["feedback"])