import csv
import requests
from bs4 import BeautifulSoup

with open('./result1.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
                     'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
                     'Ссылка на карточку с товаром'])

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')

schema = 'https://parsinger.ru/html/'

pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

for item in pagen:
    response = requests.get(f'{schema}{item}')

    soup = BeautifulSoup(response.text, 'lxml')
    watch_list = [link['href'] for link in soup.find('div', class_='item_card').find_all('a', class_='name_item')]
    for url in watch_list:
        response = requests.get(f'{schema}{url}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = soup.find('p', id='p_header').text.strip()
        article = soup.find('p', class_='article').text.split(':')[1]
        description = [x.text.split('\n') for x in soup.find_all('ul', id='description')]
        in_stock = soup.find('span', id='in_stock').text.split(':')[1]
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        link = f'{schema}{url}'

        descr = [x.split(': ')[1].strip() for x in description[0] if x]

        with open('./result1.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([name, article, *descr, in_stock, price, old_price, link])
