from urllib.request import urlopen
from bs4 import BeautifulSoup
from bookscraper.book import Book

class Parser:
    def __init__(self, url, name, search_url):
        self.url = url
        self.name = name
        self.search_url = search_url


class DatabazeKnih(Parser):

    PAGE_URL = 'http://www.databazeknih.cz/'
    NAME = 'Databáze knih'
    SEARCH_URL = 'search?q={}&hledat=&stranka=search'

    def __init__(self):
        super().__init__(DatabazeKnih.PAGE_URL, DatabazeKnih.NAME, DatabazeKnih.SEARCH_URL)

    def search(self, name):
        self.search_html = urlopen(DatabazeKnih.PAGE_URL + DatabazeKnih.SEARCH_URL.format(name))
        self.book_link = self.get_book_link()
        return self.get_book_info()

    def get_book_page(self, link):
        return urlopen(DatabazeKnih.PAGE_URL + link)

    def get_book_link(self):
        soup = BeautifulSoup(self.search_html, 'html.parser')
        return soup.find(type='book').attrs['href']

    @staticmethod
    def get_comments(soup):
        comments = soup.find_all('div', {'class': 'komholdu'})

    def get_book_info(self):
        soup = BeautifulSoup(self.self.book_link, 'html.parser')
        title = soup.find(itemprop='name').attrs['itemprop']
        rating = soup.findAll('a', {'class': 'bpoints'})[0].string
        text = soup.find(id='jl').string   # ?show=alldesc
        author = soup.find_all('p', {'class': 'new2'})
        year = soup.find(itemprop='datePublished').string
        comments = DatabazeKnih.get_comments(soup)

