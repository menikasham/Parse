import pprint

import requests
from bs4 import BeautifulSoup
import json

schema = 'https://parsinger.ru/html/'
result_json = []
cat_dict = {'index1': 'Часы', 'index2': 'Телефоны', 'index3': 'Мышки', 'index4': 'HDD', 'index5': 'Наушники'}

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')

goods = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]

for item in goods:
    dkey = item.split("_")[0]
    response = requests.get(f'{schema}{item}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

    for item1 in pagen:
        response = requests.get(f'{schema}{item1}')
        soup = BeautifulSoup(response.text, 'lxml')
        goods_list = [link['href'] for link in soup.find('div', class_='item_card').find_all('a', class_='name_item')]

        for url in goods_list:
            descr = {}
            response = requests.get(f'{schema}{url}')
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            name = soup.find('p', id='p_header').text.strip()
            article = soup.find('p', class_='article').text
            in_stock = soup.find('span', id='in_stock').text
            price = soup.find('span', id='price').text
            old_price = soup.find('span', id='old_price').text

            description = [x.text.strip().split('\n') for x in soup.find_all('ul', id='description')][0]
            link = f'{schema}{url}'

            for i in range(len(description)):
                descr[f'{description[i].split(":")[0].strip()}'] = f'{description[i].split(":")[1].strip()}'

            result_json.append({
                'categories': cat_dict[dkey],
                'name': name,
                'article': article.split(":")[1].strip(),
                'description': descr,
                'in_stock': in_stock.split(":")[1].strip(),
                'price': price,
                'old_price': old_price,
                'link': link,
            })

            with open('res1.json', 'w', encoding='utf-8') as file:
                json.dump(result_json, file, indent=4, ensure_ascii=False)
