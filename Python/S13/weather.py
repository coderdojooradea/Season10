import requests
import streamlit as st

geo_url = "http://api.openweathermap.org/geo/1.0/direct?"
weather_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "6c64d4a25dfad806e5ef1cddae5a5acf"

def get_lat_lon(city, key):
    geo_url_ll = geo_url +f"q={city}&limit=3&appid={key}"
    # print(geo_url_ll)
    response = requests.get(geo_url_ll)
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    return city, lat, lon

def get_weather_ll(lat, lon, key):
    ll_url = weather_url + f"lat={lat}&lon={lon}&appid={key}"
    response = requests.get(ll_url)
    print(response.json())
    weather = response.json()['weather'][0]
    description = weather['main']
    icon = weather['icon']
    main= response.json()['main']
    temp = main['temp']
    pres = main['pressure']
    hum = main['humidity']
    wind = response.json()['wind']['speed']
    resolution = {'descrition': description,
                  'icon': icon, 
                  'temp': temp, 
                  'pressure':pres, 
                  'humidity': hum, 
                  'wind': wind}
    return resolution 

def display_weather(data):
    st.title = "Weather data"


if __name__ == 'main':
    city, lat, lon = get_lat_lon("Oradea", api_key)
    wdata = get_weather_ll(lat, lon, api_key)
    display_weather(wdata)
