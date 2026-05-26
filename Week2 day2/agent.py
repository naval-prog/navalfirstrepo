from dotenv import load_dotenv
load_dotenv()

import os
import requests

from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from tavily import TavilyClient
from rich import print


# -------------------- TOOLS --------------------

# Weather Tool
@tool
def get_weather(city: str) -> str:
    """Get current weather of a city"""

    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        return f"Weather in {city}: {temp}°C, {condition}"

    return "Weather data not found."


# Tavily Search Tool
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web using Tavily"""

    result = tavily_client.search(query=query)

    return str(result)


# -------------------- LLM --------------------

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

tools = [get_weather, web_search]

llm_with_tool = llm.bind_tools(tools)


# -------------------- CHAT LOOP --------------------

messages = []

print("[bold green]City Intelligence System[/bold green]")
print("[yellow]Type 'exit' to quit[/yellow]")

while True:

    user_input = input("You : ")

    if user_input.lower() == "exit":
        break

    messages.append(HumanMessage(content=user_input))

    while True:

        result = llm_with_tool.invoke(messages)

        messages.append(result)

        # Tool required
        if result.tool_calls:

            for tool_call in result.tool_calls:

                tool_name = tool_call["name"]

                # HUMAN IN THE LOOP
                confirm = input(
                    f"Agent wants to call '{tool_name}'. Approve? (yes/no): "
                )

                if confirm.lower() == "no":
                    print("Tool call denied.")

                    messages.append(
                        ToolMessage(
                            content="Tool call denied by user.",
                            tool_call_id=tool_call["id"]
                        )
                    )
                    break

                # Execute tool
                selected_tool = {
                    "get_weather": get_weather,
                    "web_search": web_search
                }[tool_name]

                tool_result = selected_tool.invoke(tool_call["args"])

                messages.append(
                    ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
                    )
                )

        else:
            print("\nAI :", result.content)
            break