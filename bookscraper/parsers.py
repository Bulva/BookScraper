from urllib.request import urlopen
from bs4 import BeautifulSoup
from bookscraper.book import Book
from bookscraper.comment import Comment


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
        self.book_link = DatabazeKnih.PAGE_URL + self.get_book_link() + '?show=alldesc'
        return self.get_book_info()

    def get_book_page(self):
        return urlopen(self.book_link)

    def get_book_link(self):
        soup = BeautifulSoup(self.search_html, 'html.parser')
        return soup.find(type='book').attrs['href']

    @staticmethod
    def parse_comment(comment):
        user = comment.find('a').string
        text = comment.find('p', {'class': 'odtopm new2 justify'}).text
        date = comment.find('span', {'class': 'pozn_lightest odleft_pet'}).string
        return user, text, date

    @staticmethod
    def get_comments(soup):
        comments_objects = []
        comments = soup.find_all('div', {'class': 'komholdu'})
        for comment in comments:
            user, text, date = DatabazeKnih.parse_comment(comment)
            comments_objects.append(Comment(user, text, date))
        return comments_objects

    @staticmethod
    def get_authors(soup):
        return [author.string for author in soup.find(itemprop='author').find_all('a')]

    def get_book_info(self):
        soup = BeautifulSoup(self.get_book_page(), 'html.parser')
        title = soup.find(itemprop='name').string
        rating = soup.findAll('a', {'class': 'bpoints'})[0].string
        text = soup.find(itemprop='description').string
        authors = DatabazeKnih.get_authors(soup)
        year = soup.find(itemprop='datePublished').string
        comments = DatabazeKnih.get_comments(soup)
        return Book(title, rating, text, authors, year, comments)
