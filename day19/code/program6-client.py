import requests
import pandas as pd

# set the url
URL = "http://localhost:5200/todo"

def get_all_todo_items():
    # send the GET request
    response = requests.get(URL)

    # get the status code
    # print(response.status_code)

    # get the result
    df = pd.DataFrame(response.json())
    print(df)

get_all_todo_items()
