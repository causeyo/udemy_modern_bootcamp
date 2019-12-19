import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
    response = requests.get(base_url+url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        all_quotes.append({
            "text":quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    # sleep(2)

quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote: ")
print(quote["text"])
print(quote["author"])
guess = ''
while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input("Who said this quote? Guesses remaining {}\n".format(remaining_guesses))
    if guess.lower() == quote["author"].lower():
        print("THAT'S THE TRUTH, RUTH!!!")
        break
    remaining_guesses -= 1
    if remaining_guesses == 3:
        res = requests.get(base_url+quote['bio-link'])
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print("HINT!!! The author's was born on {} {}".format(birth_date, birth_place))
    elif remaining_guesses == 2:
        print("HINT!!! The author's first name starts with {}".format(quote["author"][0]))
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print("HINT!!! The author's last name starts with {}".format(last_initial))
    else:
        print("Sorry you ran out of guesses. The answer was: {}".format(quote["author"]))
