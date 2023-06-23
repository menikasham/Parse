# -*- coding: utf-8 -*-
import os

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv

ua = UserAgent()


URL = 'https://auto.ria.com/newauto/marka-bogdan'
HEADERS = {'User-Agent': ua.random}
HOST = 'https://auto.ria.com'
FILE = f'cars_{URL.split("-")[1]}.csv'

resp = requests.get(URL, headers=HEADERS)


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'lxml')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('section', class_='proposition')
    cars = []
    for item in items:
        try:
            ua_price = item.find('span', class_='size16')
            if ua_price:
                ua_price = ua_price.get_text(strip=True)
            else:
                ua_price = 'Цена уточняется'
            cars.append({
                'title': item.find('div', class_='proposition_title').get_text(strip=True),
                'link': HOST + item.find('a', attrs={'class': 'proposition_link'}).get('href'),
                'usd_price': item.find('span', class_='green').get_text(strip=True),
                'grv_price': ua_price,
                'city': item.find('span', class_='region').get_text()
            })
        except:
            continue
    return cars


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Цена USD', 'Цена UAH', 'Город'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_price'], item['grv_price'], item['city']])


def parse():
    URL = input('URL: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        save_file(cars, FILE)
        os.startfile(FILE)
        print(f'Найдено {len(cars)} машин')

    else:
        print('Error')
    return


parse()
