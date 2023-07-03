import requests
from bs4 import BeautifulSoup
import json

schema = 'https://parsinger.ru/html/'
result_json = []

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')

pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

for url in pagen:
    response = requests.get(f'{schema}{url}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    article = [x.text.strip() for x in soup.find_all('p', class_='article')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]
    old_price = [x.text for x in soup.find_all('p', class_='price')]
    print(article)
    for list_item, price_item, name, article in zip(description, price, name, article):
        result_json.append({
            'name': name,
            f'{article}'
            f'{list_item[0].split(":")[0].strip()}': list_item[0].split(':')[1].strip(),
            f'{list_item[1].split(":")[0].strip()}': list_item[0].split(':')[1].strip(),
            f'{list_item[2].split(":")[0].strip()}': list_item[0].split(':')[1].strip(),
            f'{list_item[3].split(":")[0].strip()}': list_item[0].split(':')[1].strip(),
            'price': price_item
        })
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
