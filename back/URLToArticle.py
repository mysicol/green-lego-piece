import requests
from bs4 import BeautifulSoup

class URLToArticle:
    def __init__(self, website_link):
        self._link = website_link
    
    def read(self):
        raw_page = requests.get(self._link)
    
        soup = BeautifulSoup(raw_page.text)

        soup_pretty = BeautifulSoup(soup.prettify())

        strings = soup_pretty.get_text().split('\n')

        strings_better = list(filter(lambda s: (len(s) > 20), strings))

        strings_even_better = list(map(str.strip, strings_better))

        return " ".join(strings_even_better)