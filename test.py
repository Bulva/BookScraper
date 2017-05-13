from bookscraper.parsers import DatabazeKnih

parser = DatabazeKnih()
book = parser.search('ydris')  # Name of the book
for comment in book.comments:
    print(comment.date)
