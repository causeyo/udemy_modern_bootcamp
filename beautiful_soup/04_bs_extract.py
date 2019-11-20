import requests
from bs4 import BeautifulSoup
import csv

# web_page = "https://www.betexplorer.com/soccer/poland/ekstraklasa/results/"
web_page = "https://www.rithmschool.com/blog"

response = requests.get(web_page)
# print(response.text) # whole html -> we don't want it

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
