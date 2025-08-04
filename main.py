from fastapi import FastAPI
from datetime import datetime
import socket
import requests
import os


app = FastAPI()
VERSION = "v1.0.0"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid={WEATHER_API_KEY}&units=metric"

@app.get("/api/hello")
def hello():
    try:
        weather_data = requests.get(WEATHER_API_URL).json()
        temperature = weather_data["main"]["temp"]
    except:
        temperature = "N/A"

    return {
        "hostname": socket.gethostname(),
        "datetime": datetime.now().strftime("%y%m%d%H%M"),
        "version": VERSION,
        "weather": {
            "dhaka": {
                "temperature": temperature,
                "temp_unit": "c"
            }
        }
    }

@app.get("/api/health")
def health():
    try:
        r = requests.get(WEATHER_API_URL)
        status = "healthy" if r.status_code == 200 else "unhealthy"
    except:
        status = "unhealthy"

    return {
        "status": status
    }

