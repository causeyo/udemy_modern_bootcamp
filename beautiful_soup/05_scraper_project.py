import random
import requests
from bs4 import BeautifulSoup


def get_quotes(web_page):
    quotes_list = []
    while web_page:
        response = requests.get(web_page)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        quotes_list += scrape(quotes)
        next_button = soup.find(class_="next")
        if next_button:
            next_href = next_button.find("a")['href']
            web_page = "http://quotes.toscrape.com" + next_href
        else:
            web_page = False
    return quotes_list


def scrape(elements):
    data = []
    for element in elements:
        text = element.find(class_="text")
        text = text.get_text()
        author = element.find(class_="author")
        author = author.get_text()
        href = element.find("a")['href']
        data.append(
            {
                'author': author,
                'quote': text,
                'href': href
            }
        )
    return data


def scrape_born_data(author_href):
    response = requests.get("http://quotes.toscrape.com" + author_href)
    soup = BeautifulSoup(response.text, "html.parser")
    borndate = soup.find(class_="author-born-date").get_text()
    bornplace = soup.find(class_="author-born-location").get_text()
    return "This person was born on {} {}".format(borndate, bornplace)


def main():
    html_link = "http://quotes.toscrape.com"
    work_list = get_quotes(html_link)
    quote_dict = random.choice(work_list)
    # print(quote_dict)
    tries = 4
    while tries >= 0:
        if tries == 4:
            guess = input("Who said: {}: \nYour answer: ".format(quote_dict['quote']))
            tries -= 1
        elif tries == 3:
            guess = input("{} \nYour answer: ".format(scrape_born_data(quote_dict['href'])))
            tries -= 1
        elif tries == 2:
            guess = input("First name starts with lettter '{}'\nYour answer: ".format(quote_dict['author'][0]))
            tries -= 1
        elif tries == 1:
            guess = input("Last name starts with lettter '{}'\nYour answer: ".format(quote_dict['author'].split()[1][0]))
            tries -= 1
        elif tries == 0:
            print("Correct answer: {}".format(quote_dict['author']))
            play = input("do you wanna play again(y/n)? ")
            if play == 'y':
                tries = 4
                quote_dict = random.choice(work_list)
            else:
                print("\nSEE YOU LATER!!!\n")
                break

        if guess == quote_dict['author']:
            print("YOU WON!")
            tries = 0


if __name__ == '__main__':
    main()


