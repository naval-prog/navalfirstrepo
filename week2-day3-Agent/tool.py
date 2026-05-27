from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str)->str:
    """search the web for recent and relaible information on a topic .return tille ,url and web scraping"""

    results=tavily.search(query=query,max_result=5)
    
    out=[]

    for r in results['results']:
        out.append(
            f"Tiittle:{r['title']}\nURL:{r['url']}"
        )

    return "\n----\n".join(out)

@tool
def scrape_url(url:str)->str:
    """Scrape and result clean text content from a given url for depper reading """
    try:
        resp=requests.get(url,timeout=8,header={"user-Agent":"Mozila/5.0"})
        soup=BeautifulSoup(resp.txt,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=TRUE)[:3000]
    except Exception as e:
        return f"could not scarape Url:{str(e)}"


print(scrape_url.invoke("https://www.livehindustan.com/"))    
