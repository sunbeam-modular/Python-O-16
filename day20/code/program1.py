# pip install beautifulsoup4

# import BeautifulSoup from bs4
from bs4 import BeautifulSoup

# read the contents from the file
with open('test_website.html', 'r') as file:
    contents = file.read()

# create a soup object from the contents
# param1: html source
# param2: 
# - parser to use to parse the contents
# - program used to understand the format in the contents
# contains the object of the html DOM (document object model)
soup = BeautifulSoup(contents, "html.parser")

# print(soup)

def function1():
    # find the contents of h1
    h1 = soup.find('h1')
    print(h1)
    print(f"contents of h1 = {h1.text}")

# function1()

def function2():
    # get all the list items
    items = soup.find_all('li')

    # collect all the quotes
    quotes = []
    for item in items:
        quotes.append(item.text.strip())
    print(quotes)

function2()