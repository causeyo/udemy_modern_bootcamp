import requests
from bs4 import BeautifulSoup

web_page = "http://quotes.toscrape.com/"

response = requests.get(web_page)
# print(response.text) # whole html -> we don't want it

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all(class_="quote")
for quote in quotes:
    text = quote.find(class_="text")
    text = text.get_text()
    author = quote.find(class_="author")
    author = author.get_text()
    href =
    print("{} said {}".format(author, text))
    print(10*"x")

    # for article in articles:
    #     a_tag = article.find("a")
    #     title = a_tag.get_text()
    #     url = a_tag['href']
    #     date = article.find("time")["datetime"]
    #     csv_writer.writerow([title, url, date])