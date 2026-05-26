from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda

model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq"
)
parser=StrOutputParser()

short_prompt=ChatPromptTemplate.from_template(
  "Explain {topic}in 1-2 lines"
)
detailed_prompt=ChatPromptTemplate.from_template(
  "Explain {topic} in detail"
)
topic="machine learning "

chain=RunnableParallel({
  "short":RunnableLambda(lambda x:x['short'])|short_prompt | model| parser,
  "detailed":RunnableLambda(lambda x:x['detailed'])|detailed_prompt |model|parser
})
result=chain.invoke({
     "short":{"topic":"Machine learning"},
     "detailed":{"topic":"deeplearning"}
})

print(result['short'])
print(result['detailed'])

