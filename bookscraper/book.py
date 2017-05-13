class Book:
    def __init__(self, title, rating, text, author, year):
        self.title = title
        self.rating = rating
        self.text = text
        self.author = author
        self.year = year
        self.comments = []