import requests
from bs4 import BeautifulSoup
import json
import pprint

schema = 'https://parsinger.ru/html/'
result_json = []

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')
# name, article, description, in_stock, price, old_price, link = [], [], [], [], [], [], []

pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

for item1 in pagen:
    response = requests.get(f'{schema}{item1}')
    soup = BeautifulSoup(response.text, 'lxml')
    goods_list = [link['href'] for link in soup.find('div', class_='item_card').find_all('a', class_='name_item')]

    for url in goods_list:
        link = []
        response = requests.get(f'{schema}{url}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')


        # description.append([x.strip() for x in [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')][0] if x])
        description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]

        link.append(f'{schema}{url}')

        for descr, link in zip(description, link):
            descr = [value for value in descr if value]
            print(descr)


            result_json.append({
                'Категория': 'часы',
                'Наименование': descr[0],
                f'{descr[1].split(":")[0].strip()}': f'{descr[1].split(":")[1].strip()}',
                'Описание': {},
                f'{descr[2].split(":")[0].strip()}': f'{descr[2].split(":")[1].strip()}',
                f'{descr[3].split(":")[0].strip()}': f'{descr[3].split(":")[1].strip()}',
                f'{descr[4].split(":")[0].strip()}': f'{descr[4].split(":")[1].strip()}',
                f'{descr[5].split(":")[0].strip()}': f'{descr[5].split(":")[1].strip()}',
                f'{descr[6].split(":")[0].strip()}': f'{descr[6].split(":")[1].strip()}',
                f'{descr[7].split(":")[0].strip()}': f'{descr[7].split(":")[1].strip()}',
                f'{descr[8].split(":")[0].strip()}': f'{descr[8].split(":")[1].strip()}',
                f'{descr[9].split(":")[0].strip()}': f'{descr[9].split(":")[1].strip()}',
                f'{descr[10].split(":")[0].strip()}': f'{descr[10].split(":")[1].strip()}',
                'Цена': f'{descr[11]}',
                'Старая цена': f'{descr[12]}',
                'Адрес карточки': link,

            })
        pprint.pprint(result_json)
        with open('res.json', 'w', encoding='utf-8') as file:
            json.dump(result_json, file, indent=4, ensure_ascii=False)
# descr = [x.split(': ')[1].strip() for x in description[0] if x]

        # name.append(soup.find('p', id='p_header').text.strip())
        # article.append(soup.find('p', class_='article').text)
        # in_stock.append(soup.find('span', id='in_stock').text)
        # price.append(soup.find('span', id='price').text)
        # old_price.append(soup.find('span', id='old_price').text)