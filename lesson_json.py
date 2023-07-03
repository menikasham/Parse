import requests
from bs4 import BeautifulSoup
import json

schema = 'https://parsinger.ru/html/'
result_json = []

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')
pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

for item in pagen:
    response = requests.get(f'{schema}{item}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    for list_item, price_item, name in zip(description, price, name):
        result_json.append({
            'name': name,
            'brand': list_item[0].strip().split()[1],
            'type': list_item[1].strip().split(': ')[1],
            'material': list_item[2].strip().split(': ')[1],
            'tech': list_item[3].strip().split(": ")[1],
            'price': price_item

        })
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
