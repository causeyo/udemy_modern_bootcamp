import sqlite3
import requests
from bs4 import BeautifulSoup


web_page = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"
# Requests url
response = requests.get(web_page)

print(response)