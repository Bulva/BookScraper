class Parser:
    def __init__(self, url, name):
        self.url = url
        self.name = name


class DatabazeKnih(Parser):

    PAGE_URL = 'http://www.databazeknih.cz/'
    NAME = 'Databáze knih'

    def __init__(self):
        super().__init__(DatabazeKnih.PAGE_URL, DatabazeKnih.NAME)