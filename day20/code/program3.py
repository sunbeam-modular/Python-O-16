from bs4 import BeautifulSoup
import requests
import pandas as pd

# website to scrape
url = "https://quotes.toscrape.com/"

# get the contents of required website
response = requests.get(url)

# collect all the quotes
quotes = []

if response.status_code == 200:
    # create the soup
    soup = BeautifulSoup(response.text, "html.parser")

    # find the quotes from div having class 'quote'
    div_elements = soup.find_all('div', class_="quote")

    # get the quotes from every div element
    for div in div_elements:

        # find the quote span from the div element
        span = div.find('span', class_='text')

        # find the author small element from div
        small = div.find('small', class_='author')

        # collect the quote
        quotes.append({
            "quote": span.text.replace("“", '').replace("”", '').strip(),
            "author": small.text.strip()
        })

    # create a data frame from quotes
    df = pd.DataFrame(quotes)
    print(df)

    # save the contents to a csv file
    df.to_csv("quotes.csv", index=False)
else:
    print("Error while getting the contents of website")