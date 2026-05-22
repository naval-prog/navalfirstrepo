import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from models import Post

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = FastAPI()

URL = "https://jsonplaceholder.typicode.com/posts"

@app.get("/posts")
def get_posts():
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()

        data = response.json()

        validated_posts = [
            Post(**post).model_dump()
            for post in data
        ]

        return {
            "success": True,
            "data": validated_posts
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }