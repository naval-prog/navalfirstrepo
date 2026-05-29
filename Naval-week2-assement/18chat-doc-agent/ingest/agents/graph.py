from langchain_groq import ChatGroq
from agent.retrieve import retrieve_docs
from agent.tools import current_time
from agent.state import AgentState

llm = ChatGroq(
    model="llama3-70b-8192",
    api_key="GROQ_KEY"
)

def agent_node(state: AgentState):

    q = state["question"]

    keywords = ["what", "explain", "describe"]

    use_retrieval = any(k in q.lower() for k in keywords)

    return {
        **state,
        "use_retrieval": use_retrieval
    }