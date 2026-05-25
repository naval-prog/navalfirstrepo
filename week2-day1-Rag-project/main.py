from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.document_loaders import WebBaseLoader --load from website 
# from langchain_community.document_loaders import pdfLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

data=PyPDFLoader("documentLoader/ai.pdf")
docs =data.load()

splitter=RecursiveCharacterTextSplitter(
  chunk_size=100,
  chunk_overlap=12
)

chunks=splitter.split_documents(docs)
template=ChatPromptTemplate.from_messages(
  [
    ("system","you are a AI that sumarize the text"),
    ("human","{data}")
  ]
)

model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq",
     temperature=0.7,
     max_tokens=20
)
prompt=template.format_messages(data=docs)
response = model.invoke(prompt)
print(response.content)