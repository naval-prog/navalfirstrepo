from weather_service import fect_weather
from models import WeatherMOdel
from report import save_report

def main():
  city=input("enter the city")
  try:
    raw_data=fect_weather(city)

    weather=WeatherMOdel(**raw_data)

    print("/n weather data")
    print(weather)

    save_report(weather.model_dump())

  except:
    print("error",e)


if __name__=="__main__":
  main()    


