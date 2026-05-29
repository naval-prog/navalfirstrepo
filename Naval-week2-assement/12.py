from typing import TypeDist
from langgraph.graph import StateGraph,START,END

class MyState(TypeDist):
  messages:list


def greet(state:MyState):
  state["messages"].append("Hello!")
  return state

def farewell(state:MyState):
  state["messages"].append("byee")
  return state

builder=StateGraph(MyState)

builder.add_node("greet",greet)
builder.add_node("farewaal",farewell)

builder.add_edge(START,"greet")
builder.add_edge("greet","farewall")
builder.add_edge("farewell",END)

graph=builder.compile()

result=graph.invoke(
  {"messages":[]}
)
print(result)

