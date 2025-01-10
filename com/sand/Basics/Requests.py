import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
peoples = json['people']

for p in peoples:
    print(p['name'])