import json 
from datetime import datetime

def save_report(weather_data,filename="weather_reprot.json"):
  report={
    "timestamp":str(datetime.now()),
    "date":weather_data
  }

  with open(filename,"w")as f:
    json.dump(report,f,indent=4)

  print("report saved sucesfully")  