import csv
import requests
from bs4 import BeautifulSoup

with open('./result2.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена',
                     'Ссылка на карточку с товаром'])

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')

schema = 'https://parsinger.ru/html/'
goods = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]

for item in goods:
    response = requests.get(f'{schema}{item}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

    for item1 in pagen:
        response = requests.get(f'{schema}{item1}')
        soup = BeautifulSoup(response.text, 'lxml')
        goods_list = [link['href'] for link in soup.find('div', class_='item_card').find_all('a', class_='name_item')]

        for url in goods_list:
            response = requests.get(f'{schema}{url}')
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            name = soup.find('p', id='p_header').text.strip()
            article = soup.find('p', class_='article').text.split(':')[1]
            brand = soup.find('li', id='brand').text.split(':')[1]
            model = soup.find('li', id='model').text.split(':')[1]
            in_stock = soup.find('span', id='in_stock').text.split(':')[1]
            price = soup.find('span', id='price').text
            old_price = soup.find('span', id='old_price').text
            link = f'{schema}{url}'

            with open('./result2.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow([name, article, brand, model, in_stock, price, old_price, link])
