import requests

geo_url = "http://api.openweathermap.org/geo/1.0/direct?"
url = "https://api.openweathermap.org/data/3.0/onecall?"
api_key = "6c64d4a25dfad806e5ef1cddae5a5acf"

def get_lat_lon(city, key):
    geo_url_ll = geo_url +f"q={city}&limit=3&appid={key}"
    # print(geo_url_ll)
    response = requests.get(geo_url_ll)
    return response.json()

def get_weather_city(city, api_key):
    # city_url = url+f"q={city}&appid"
    pass


print(get_lat_lon("Oradea", api_key))
