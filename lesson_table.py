import csv
import requests
from bs4 import BeautifulSoup

# with open('./result.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена'])

response = requests.get('https://parsinger.ru/html/index4_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')

schema = 'https://parsinger.ru/html/'

goods = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]

for item in goods:
    response = requests.get(f'{schema}{item}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    for url in pagen:
        response = requests.get(f'{schema}{url}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        print(description)

        # for item, descr, price in zip(name, description, price):
        #     flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
        #
        #     with open('./result.csv', 'a', encoding='utf-8', newline='') as f:
        #         writer = csv.writer(f, delimiter=';')
        #         writer.writerow(flatten)

#
# soup = BeautifulSoup(response.text, 'lxml')
# print(sum(set([float(txt.text) for txt in soup.find_all('td')])))
# qwe = sum([float(i.text) for i in soup.select('td:first-child')])
# print(sum([float(txt.text) for txt in soup.find_all('td', class_='green')]))

# num1 = [float(i.text) for i in soup.find_all('td', class_="orange")]
# num2 = [int(i.text) for i in soup.select('td:last-child')]
#
# answer = np.array(num1) @ np.array(num2)
# print(answer)


# for i in range(1, 16):
#     result[f'{i} column'] = round(sum([float(j.text) for j in soup.select(f'td:nth-child({i})')]), 3)
# print(result)
