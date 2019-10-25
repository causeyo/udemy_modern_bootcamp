# query string -> "http://www.example.com?key1=value1&key2=value2"
# it is this part after question mark
# we can check options for requests on "https://icanhazdadjoke.com/api"



import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

data = response.json()
print(data['results'])

# print(data["joke"])
# print("status of response is {}".format(data["status"]))