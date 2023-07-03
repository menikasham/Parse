from bs4 import BeautifulSoup
import requests

names = []
count =0
cost_all = 0
url = 'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = f'http://parsinger.ru/html/'
urls = (tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a'))
print(urls)

for item in urls:
    response = requests.get(f'{schema}{url}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    mouses = (tag['href'] for tag in soup.find_all('a', {'class': 'name_item'}))
    for u in mouses:
        response = requests.get(f'{schema}{u}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        art = [int(txt.text.split()[1]) for txt in soup.find_all(class_="article")]
        for i in art:
            prin

from bs4 import BeautifulSoup
import requests

pagen = 4
names = []
url = 'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = f'http://parsinger.ru/html/'
urls = (tag['href'] for tag in soup.find('div', class_='nav_menu').find_all('a'))

for url in urls:

    response = requests.get(f'{schema}{url}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    urls_pag = (tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a'))
    for item in urls_pag:
        response = requests.get(f'{schema}{item}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        items = (tag['href'] for tag in soup.find_all('a', {'class': 'name_item'}))
        for u in items:
            response = requests.get(f'{schema}{u}')
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            name = soup.find('p', id='p_header').text
            quantity = int(soup.find('span', id="in_stock").text.split()[2])
            price = int(soup.find('span', id="price").text.split()[0])
            qwe = quantity * price
            cost_all += qwe

print(cost_all)
#     for u in mouses:
#         response = requests.get(f'{schema}{u}')
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         art = int(soup.find(class_="article").text.split()[1])
#         names.append(art)
#
# print(sum(names))

# price = int(soup.find('span', id='price').text.split(" ")[0])
# old_price = int(soup.find('span', id='old_price').text.split(" ")[0])
# disc = (old_price - price) * 100 / old_price
# print(disc)
