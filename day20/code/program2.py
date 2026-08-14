from bs4 import BeautifulSoup
import requests

# website to scrape
url = "https://quotes.toscrape.com/"

# get the contents of required website
response = requests.get(url)

if response.status_code == 200:
    # create the soup
    soup = BeautifulSoup(response.text, "html.parser")

    # find the quotes from span having class 'text'
    span_elements = soup.find_all('span', class_="text")

    # get the quotes from every span element
    for span in span_elements:
        print(span.text.strip())

else:
    print("Error while getting the contents of website")