# pip install python-dotenv

import requests
from dotenv import load_dotenv
import os

# load all the settings from .env file
# and create environment variables for all of them
load_dotenv()

# read the value of a required environment
# define the configuration parameters
URL = os.environ['URL']
API_KEY = os.environ['API_KEY']

def function1(city):
    # send a GET request to get the weather response
    response = requests.get(f"{URL}?appid={API_KEY}&units=metric&q={city}")

    # get the response status code
    print(f"status = {response.status_code}")

    # get the weather information from response
    print(response.json())

# function1("pune")
function1("mumbai")