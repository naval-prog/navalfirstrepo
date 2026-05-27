from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tool import web_search,scrape_url
import os
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq"
)

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )


def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

writer_prompt=ChatPromptTemplate.from_messages([
    ("system","you are an expert reasearch writer.writer clear,structured and insightfull"),
    (
        "human","""
        write  a deatiled research report on the topic below
        Topic:{topic}
        reacserch gathered:
        {research}
        structure the report as :
        -Introduction
        -key findings (minimum 3 well-explaned points)
        -conclusion 
        -sources (list all urls  found int he reasearch )
        Be detailed ,factual and professional
        """
    ),
])

writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
