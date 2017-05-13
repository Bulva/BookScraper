BookScraper is a Python library that parser information about books from czech book servers (databazeknih.cz, cbdb.cz)

```python
from bookscraper.parsers import DatabazeKnih

parser = DatabazeKnih()
link = parser.search('ydris')  # Name of the book
```