import requests
from bs4 import BeautifulSoup
import csv

# web_page = "https://www.betexplorer.com/soccer/poland/ekstraklasa/results/"
web_page = "https://www.rithmschool.com/blog"

response = requests.get(web_page)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
data = soup.find_all("tr")
# data = soup.find_all(class_="border_right_bottom")
for elem in data:
    print(elem)
