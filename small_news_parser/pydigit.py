from bs4 import BeautifulSoup as bs
import requests
import pprint


url = 'https://pythondigest.ru/feed/?q=neural+network'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

output = {}
news_containers = soup.find_all('div', class_='item-container')
for news in news_containers[:5]:
    data = news.find_next('small').text[2:12]
    theme = str(news.find_next('div', class_='news-line-item').text)
    href_data = news.find_next('div', class_='news-line-item')
    href_data = href_data.find('a')
    href = href_data.get('href')
    # pprint.pprint(data)
    # pprint.pprint(href)
    # pprint.pprint(theme)
    # pprint.pprint(news)
    response = requests.get(href)
    soup = bs(response.text, 'html.parser')
    all_text = soup.find_all('p')
    text = ''
    content = []
    content.append(data)
    for p in all_text:
        text += ''.join(p.text.replace('\t','').replace('\n','').replace('\r',''))
    content.append(text)
    output[theme] = content

for k, v in output.items():
    print(k)
    pprint.pprint(v)
    print()
