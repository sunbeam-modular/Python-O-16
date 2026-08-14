from bs4 import BeautifulSoup
import requests
import json

# website to scrape
url = "https://books.toscrape.com/"

def get_book_links():
    # get the contents of required website
    response = requests.get(url)

    # collect the books links
    links= []

    if response.status_code == 200:
        # create the soup
        soup = BeautifulSoup(response.text, "html.parser")

        # find the ol element from having class 'row'
        ol = soup.find('ol', class_="row")

        # find the li elements from ol
        list_items = ol.find_all('li')

        # get the book info from list_items
        for list_item in list_items:

            # find the anchor tag which contains the title
            a = list_item.find('a')

            # find the url of every book
            links.append(a.get('href'))

    else:
        print("Error while getting the contents of website")

    return links


def get_book_info(link):
    print(f"sending request to = {link}")
    # send the request to the book url
    book_url = f"{url}{link}"

    # get the contents of required website
    response = requests.get(book_url)

    # collect the books info
    book = {}

    if response.status_code == 200:
        # create the soup
        soup = BeautifulSoup(response.text, "html.parser")

        # find the book info div
        div = soup.find('div', class_='product_main')

        # get the book title
        title = div.find('h1')
        book['title'] = title.text

        # get the price 
        price = div.find('p', class_="price_color")
        book['price'] = price.text

        # get the description
        div_description = soup.find('div', id="product_description")

        # find all the siblings
        siblings = div_description.next_siblings
        for i, sibling in enumerate(siblings):
            if i == 1:
                book['description'] = sibling.text

        # print(f"description = {description}")
        # book['description'] = description

    return book


# collect all the books
books = []

# get all book links
links = get_book_links()

# collect all books
books = []

# get book info for every book
for link in links:
    book_info = get_book_info(link)
    books.append(book_info)

# save the json file
with open('books.json', "w") as file:
    file.write(json.dumps(books))
