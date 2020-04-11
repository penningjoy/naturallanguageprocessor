import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Biryani"
itemlist = []

def wikiscraper():
    try:
        page = requests.get(url = URL) # Get the page content
        soup = BeautifulSoup(page.text, 'html.parser')
        page_text = soup.get_text(strip = True)

        return page_text

    except:
        print("Something went wrong while the scraping.")
