import requests

response = requests.get('https://api.kodim.cz/python-data/people')

data = response.json()

print(data[0]['first_name'])