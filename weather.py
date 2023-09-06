import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key=os.getenv('API_KEY')

@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temperature:float
    humidity:int
    city:str



def get_lat_lon(city_name,country_code,API_key):
    response=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}").json()
    data=response[0]
    lat,lon=data.get('lat'),data.get('lon')
    return lat,lon

# add another route here

def get_current_weather(lat,lon,API_key):
    response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric").json()
    print(response)
    data=WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=response.get('main').get('temp'),
        humidity=response.get('main').get('humidity'),
        city=response.get('name')
        
    )#hhhbhbhbhhbhbb
    return data

def main(city_name,country_name):
    lat,lon=get_lat_lon(city_name,country_name,api_key)
    weather_data=get_current_weather(lat,lon,api_key)
    return weather_data

        


if __name__ =="__main__":

    
    lat,lon=get_lat_lon('Nairobi','Kenya',api_key)
    print(get_current_weather(lat,lon,api_key))


