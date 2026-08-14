from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# set the data for testing
data = {
    "email": "test2@test.com",
    "password": "test",
    "exptected": "Success"
}

# create the driver
driver = webdriver.Firefox()

# browse the url
driver.get("file:///Volumes/MyData/Sunbeam/2026/Feb/workshops/python/day20/code/login.html")

# sleep for 2 seconds
time.sleep(2)

# find the input element for email
email = driver.find_element(By.ID, 'email')

# enter the email in the input element
email.send_keys(data['email'])

# sleep for 2 seconds
time.sleep(2)

# find the password input element
password = driver.find_element(By.ID, 'password')

# enter the password
password.send_keys(data['password'])

# sleep for 2 seconds
time.sleep(2)

# find the button element
button = driver.find_element(By.TAG_NAME, 'button')

# click the button 
button.click()

# sleep for 2 seconds
time.sleep(2)

# find the result element
result = driver.find_element(By.ID, "result").text

# check if the result matches with the expected result
print(f"expectd: {data['exptected']}, actual: {result}")
print(f"test result = {data['exptected'] == result}")

# close the driver
driver.close()