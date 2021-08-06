import requests

response= requests.get("https://opentdb.com/api.php?amount=10&category=21&difficulty=easy")

for astronaut in response.json()[]:
    print('name', astronaut['name'],'aga',astronaut['age'])