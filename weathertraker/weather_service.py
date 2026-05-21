import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def fect_weather(city):
  params={
    "q":city,
    "applied":API_KEY,
    "units":"metric"
  }
  response =requests.get(BASE_URL,params=params,timeout=5)
  response.raise_for_status()

  data = response.json()

  return {
    "city":data["name"],
    "temperature":data["main"]["temp"],
    "feels_like":data["main"]["feels_like"],
    "humindity":data["main"]["humindity"],
    "weather":data["weather"][0]["description"],
    "wind_speed":data["wind"]["speed"]
  }
