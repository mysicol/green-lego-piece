import requests
from bs4 import BeautifulSoup

class URLToArticle:
    def __init__(self, website_link):
        self._link = website_link
        self._text = None
    
    def read(self):
        self._text = requests.get(self._link)
    
    def extract_content(self):
        soup = BeautifulSoup(self._text.text)

        soup_pretty = BeautifulSoup(soup.prettify())

        strings = soup_pretty.get_text().split('\n')

        strings_better = list(filter(lambda s: (len(s) > 20), strings))

        strings_even_better = list(map(str.strip, strings_better))

        return " ".join(strings_even_better)