import requests
import pprint

url = 'https://api.hh.ru/vacancies'

params = {
    'text': 'python developer',
    'page': 1
}

result = requests.get(url, params=params).json()

pprint.pprint(result)

items = result['items']

first = items[0]

print(first['url'])

result = requests.get(first['url'], params=params).json()

print(result)