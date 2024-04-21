import requests
from bs4 import BeautifulSoup

class URLToArticle:
    def __init__(self, website_link):
        self.__link = website_link
        print(website_link)
    
    def read(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}

        raw_page = requests.get(self.__link, headers=headers)
    
        soup = BeautifulSoup(raw_page.text)

        soup_pretty = BeautifulSoup(soup.prettify())

        strings = soup_pretty.get_text().split('\n')

        strings_better = list(filter(lambda s: (len(s) > 20), strings))

        strings_even_better = list(map(str.strip, strings_better))

        return " ".join(strings_even_better)