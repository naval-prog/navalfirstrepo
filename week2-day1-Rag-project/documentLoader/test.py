from langchain_community.document_loaders import  PyPDFLoader
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

splitter= CharacterTextSplitter(
  separator="",
  chunk_size=10,
  chunk_overlap=1
)
data=PyPDFLoader("documentLoader/ai.pdf")
docs=data.load()
chunks=splitter.split_documents(docs)
print(len(chunks))
print()
for i in chunks:
  print(i.page_content)
  print()
  print()