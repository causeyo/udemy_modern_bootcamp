import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
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
        print_hint(quote, remaining_guesses)
    again = ''
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("Goodbye!")


def print_hint(quote, remaining_guesses):
        if remaining_guesses == 3:
            res = requests.get(BASE_URL+quote['bio-link'])
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


quotes = read_quotes("quotes.csv")
start_game(quotes)
