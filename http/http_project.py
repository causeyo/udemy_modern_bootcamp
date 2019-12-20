# query string -> "http://www.example.com?key1=value1&key2=value2"
# it is this part after question mark
# we can check options for requests on "https://icanhazdadjoke.com/api"


import pyfiglet
from random import choice
import requests

url = "https://icanhazdadjoke.com/search"


def print_f(text_to_print, color="MAGENTA"):
    pyfiglet.print_figlet(text=text_to_print, colors=color)


def get_jokes(term):
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": term}
    )
    data = response.json()
    return data['results']


print_f(text_to_print="DaddyJoke90210")
topic = input("Let me tell you a joke! Give me a topic: ").lower()
jokes = get_jokes(topic)
if len(jokes) > 1:
    print("I've got {} jokes about {}. Here's one: \n{}".format(len(jokes), topic, choice(jokes)['joke']))
elif len(jokes) == 1:
    print("I've got one joke about {}. Here it is: \n{}".format(topic, jokes['joke']))
else:
    print("No jokes about {}. Please try again!".format(topic))
