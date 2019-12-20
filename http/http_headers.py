import requests


url = "https://icanhazdadjoke.com/"

# in such way it will be whole text
response = requests.get(url)
print(response.text)

# but we can take only plain text from website within using header

response_plain = requests.get(url, headers={"Accept": "text/plain"})
print(response_plain.text)

# here we have string under text
response_json = requests.get(url, headers={"Accept": "application/json"})
print(response_json.text)
print(type(response_json.text))

# here we have dict under json
response_json = requests.get(url, headers={"Accept": "application/json"})
data = response_json.json()
print(type(data))
print(data['joke'])

