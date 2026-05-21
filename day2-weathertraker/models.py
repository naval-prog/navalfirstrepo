from pydantic  import BaseModel

class WeatherMOdel(BaseModel):
  city:str
  temperature:float
  feels_like:float
  humindity:int
  weather:str
  wind_speed: float