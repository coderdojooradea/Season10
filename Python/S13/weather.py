import requests
import streamlit as st
import pydeck as pdk


geo_url = "http://api.openweathermap.org/geo/1.0/direct?"
weather_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "6c64d4a25dfad806e5ef1cddae5a5acf"

def get_lat_lon(city, key):
    geo_url_ll = geo_url +f"q={city}&limit=3&appid={key}"
    print(geo_url_ll)
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
    resolution = {'description': description,
                  'icon': icon, 
                  'temp': temp, 
                  'pressure':pres, 
                  'humidity': hum, 
                  'wind': wind}
    return resolution 


def display_map(lat, lon):
    view_state = pdk.ViewState(
        latitude = lat,
        longitude = lon,
        zoom = 11, pitch = 0
    )

    layer = pdk.Layer(
        'ScatterplotLayer',
        data = [{'position': [lon, lat], 
               'color': [255,0,0], 
               'radius': 100}],
        get_position ='position',
        get_color = 'color',
        get_radius = 'radius'       
    )

    map=pdk.Deck(
        layers = [layer],
        initial_view_state = view_state,
        map_style = 'mapbox://styles/mapbox/light-v9'
    )

    st.pydeck_chart(map)

def display_weather(data):

    # Construct the URL for the weather icon
    icon_url = f"http://openweathermap.org/img/wn/{data['icon']}.png"

    # Convert temperature from Kelvin to Celsius for display
    temp_celsius = data['temp'] - 273.15

    # Using columns to display text and image side by side
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**Description**: {data['description']}")
        st.write(f"**Temperature**: {temp_celsius:.2f}°C")
        st.write(f"**Pressure**: {data['pressure']} hPa")
        st.write(f"**Humidity**: {data['humidity']}%")
        st.write(f"**Wind Speed**: {data['wind']} m/s")
    with col2:
        st.image(icon_url, caption="Current Weather")

def main():
    """Display weather data along with the weather icon."""
    st.title("Weather Data")
    city = st.text_input("City name", "Oradea")  # Default value is "Oradea"

    if city:
        city, lat, lon = get_lat_lon(city, api_key)
        if lat and lon:
            wdata = get_weather_ll(lat, lon, api_key)
            if wdata:
                display_map(lat, lon)
                display_weather(wdata)
            else:
                st.error("Failed to retrieve weather data.")
        else:
            st.error("Failed to retrieve geographic data for the specified city.")

if __name__ == '__main__':
    main()
