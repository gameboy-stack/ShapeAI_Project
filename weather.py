import os
import requests as re
import datetime
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv('API_KEY')
city = str(input("Enter The City Name :- "))

req = re.get("""https://api.openweathermap.org/data/2.5/weather?q={}&appid={}""".format(city,api_key))
reqjson = req.json()

tempcity = (reqjson['main']['temp']) - 273.15
min_temp = (reqjson['main']['temp_min']) - 273.15
max_temp = (reqjson['main']['temp_max']) - 273.15
weather = reqjson['weather'][0]['description']
humidity = reqjson['main']['humidity']
wind_speed = reqjson['wind']['speed']

print("""
________________________________________________________________________

    Weather Report For => {} | Time : {}
________________________________________________________________________

    Weather     : {}
    Temperature : {:.2f}\N{DEGREE SIGN} C
    Temp_Range  : {:.2f}\N{DEGREE SIGN} C - {:.2f}\N{DEGREE SIGN} C
    Humidity    : {}
    Wind Speed  : {} kmph

"""
.format(city.capitalize(),datetime.datetime.now().strftime("%c"),weather,tempcity,min_temp,max_temp,humidity,wind_speed)
)

with open("Weather.txt","w") as f:
    f.write("""
________________________________________________________________________

    Weather Report For => {} | Time : {}
________________________________________________________________________

    Weather     : {}
    Temperature : {:.2f}\N{DEGREE SIGN} C
    Temp_Range  : {:.2f}\N{DEGREE SIGN} C - {:.2f}\N{DEGREE SIGN} C
    Humidity    : {}
    Wind Speed  : {} kmph


"""
.format(city.capitalize(),datetime.datetime.now().strftime("%c"),weather,tempcity,min_temp,max_temp,humidity,wind_speed)
)

