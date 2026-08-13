import streamlit as st
from dotenv import load_dotenv
import requests
import datetime
import pandas as pd
import os

# load the environment variables from .env file
load_dotenv()

# get the config parameters
URL = os.environ['URL']
API_KEY = os.environ['API_KEY']

# store all the cities in the current session
st.session_state.cities = []

# set the page configuration
st.set_page_config(
    page_icon="❄️",
    page_title="My Weather App"
)

# set the header
st.header("My Weather Application")
st.subheader("Get the weather information of any city")

def get_weather_icon(weather_id):
    print(f"weather id = {weather_id}")
    if weather_id >= 200 and weather_id < 300:
        return "⛈️" # thunderstorm
    elif weather_id >= 300 and weather_id < 400:
        return "🌧️" # Drizzle
    elif weather_id >= 300 and weather_id < 400:
        return "🌧️" # Drizzle
    elif weather_id >= 500 and weather_id < 600:
        return "🌦️" # Rain
    elif weather_id >= 600 and weather_id < 700:
        return "❄️" # Snow
    elif weather_id >= 700 and weather_id < 800:
        return "🌫️" # Fod
    else:
        return "🌈"

# get the input for a city 
city = st.text_input("Enter the city here")

# add a button to send request to the server
button_send = st.button('Get', type='primary')

# check if user clicked the button
if button_send:

    # check if the city is available
    if len(city) == 0:
        st.error("Please enter the city first")
    else:

        # add the city in the cities list
        st.session_state.cities.append(city)

        # refresh the page
        # st.rerun()

print(st.session_state.cities)

# get weather data for all the cities
for city in st.session_state.cities:

    # create the parameters list
    params = {
        "appid": API_KEY,
        "units": "metric",
        "q": city
    }
    
    # show a spinner while getting the response from server
    with st.spinner(f"Requesting current weather information of {city}"):

        # send the request and get the response
        response = requests.get(URL, params=params, timeout=180)

    # check the response status code
    if response.status_code == 200:
        # success response
        data = response.json()
        print(data['weather'])

        # get the city name
        city_name = data['name']

        # get the sunrise and sunset time
        country = data['sys']['country']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']

        # get the main weather info
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        sea_level = data['main']['sea_level']
        grnd_level = data['main']['grnd_level']

        # get the wind information
        speed = data['wind']['speed']
        deg = data['wind']['deg']

        # get the co-ordinates
        lon = data['coord']['lon']
        lat = data['coord']['lat']

        # get the weater description
        weather_description = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']

        # add a divider
        st.divider()

        # add the city name, country
        col1, col2 = st.columns([3, 1])

        # add city and country in first column
        with col1:
            st.subheader(f"{city_name}, {country}")
            st.caption(f"Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

        # show weather icon
        with col2:
            st.markdown(f"<h1>{get_weather_icon(weather_id)}</h1>", unsafe_allow_html=True)

        # show the main metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.metric("Temperature", value=temp)
        with col2: st.metric("Min Temperature", value=temp_min)
        with col3: st.metric("Max Temperature", value=temp_max)
        with col4: st.metric("Pressure", value=pressure)
        with col5: st.metric("Humidity", value=humidity)

        # show the map
        df = pd.DataFrame({
            "LAT": [lat],
            "LON": [lon]
        })
        st.map(data=df, zoom=12)

        # add a divider
        st.divider()
        
    else:
        # error response
        st.error('Error while communicating with openweathermap APIs')