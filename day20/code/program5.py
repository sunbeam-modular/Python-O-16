# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def function1():
    # get the browser instance 
    driver = webdriver.Firefox()

    # browse the url
    driver.get('https://www.google.com/')

    # sleep for 5 seconds
    time.sleep(5)

    # save the screenshot
    driver.save_screenshot("google_website.png")

    # close the driver
    driver.close()

# function1()

def function2():
    # extract the weather info from accuweather
    url = "https://www.accuweather.com/en/in/pune/204848/weather-forecast/204848"

    # collect all weather data
    weather_data = []

    # create the driver
    driver = webdriver.Firefox()

    # browse the url
    driver.get(url)

    # sleep for 5 second to load the website completely
    time.sleep(5)

    # find the div having class 'daily-list'
    div_daily_list = driver.find_element(By.CLASS_NAME, 'daily-list')

    # get all the anchor tags having temperature information
    anchor_tags = div_daily_list.find_elements(By.CLASS_NAME, 'daily-list-item')

    # get the temperature information for every row
    for anchor in anchor_tags:
        # find the date
        date = anchor.find_element(By.CLASS_NAME, 'date').text
        day, date = date.split('\n')

        # get the temperature data
        temp_hi = anchor.find_element(By.CLASS_NAME, 'temp-hi').text.replace("°", '')
        temp_low = anchor.find_element(By.CLASS_NAME, 'temp-lo').text.replace('°', '')

        # get the weather condition
        weather_condition = anchor.find_element(By.CLASS_NAME, 'phrase').text.replace('\n', ',')

        # get the precipitation
        precipitation = anchor.find_element(By.CLASS_NAME, 'precip').text.replace('%', '')

        # collect the info
        weather_info = {
            "day": day,
            "date": date,
            "temp_low": int(temp_low),
            "temp_high": int(temp_hi),
            "condition": weather_condition,
            "precipitation": precipitation
        }

        weather_data.append(weather_info)

    # close the driver
    driver.close()

    # create pandas dataframe
    df = pd.DataFrame(weather_data)
    print(df)

    # save the data as csv file
    df.to_csv("weather.csv", index=False)

function2() 