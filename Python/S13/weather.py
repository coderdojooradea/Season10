import requests
import streamlit as st
import pydeck as pdk

# URLs and API key setup
geo_url = "http://api.openweathermap.org/geo/1.0/direct?"
weather_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "6c64d4a25dfad806e5ef1cddae5a5acf"

def get_lat_lon(city, key):
    """Fetch latitude and longitude for a given city."""
    geo_url_ll = f"{geo_url}q={city}&limit=3&appid={key}"
    response = requests.get(geo_url_ll)
    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return city, lat, lon
    return None, None, None

def get_weather_ll(lat, lon, key):
    """Fetch weather data using latitude and longitude."""
    ll_url = f"{weather_url}lat={lat}&lon={lon}&appid={key}"
    response = requests.get(ll_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]
        description = weather['main']
        icon = weather['icon']
        main = data['main']
        temp = main['temp']
        pres = main['pressure']
        hum = main['humidity']
        wind = data['wind']['speed']
        resolution = {'description': description,
                      'icon': icon, 
                      'temp': temp, 
                      'pressure': pres, 
                      'humidity': hum, 
                      'wind': wind}
        return resolution
    return None


def display_map(lat, lon):
    """Display a map centered at the specified latitude and longitude."""
    view_state = pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=11,
        pitch=0
    )
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=[{'position': [lon, lat], 'color': [255, 0, 0], 'radius': 100}],
        get_position='position',
        get_color='color',
        get_radius='radius'       
    )
    map = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style='mapbox://styles/mapbox/light-v9'
    )
    st.pydeck_chart(map)


def display_weather(data):
    """Display weather data along with the weather icon."""
    st.title("Weather Data")
    icon_url = f"http://openweathermap.org/img/wn/{data['icon']}.png"
    temp_celsius = data['temp'] - 273.15  # Convert temperature from Kelvin to Celsius
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
