from auth import pref
import os
import csv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import logging
import sqlite3

load_dotenv()

logging.basicConfig(filename='wiki_parse.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

ua = UserAgent()

URL = 'https://wiki.sptlab.ru/login.action?os_destination=%2F'
HEADERS = {'User-Agent': ua.random}
exclude_list = ['SPE', 'ВИП', 'SPTS']


def get_html(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    s = Service('./chromedriver.exe')
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get(url)

    login = browser.find_element(By.NAME, 'os_username')
    insert_pass = browser.find_element(By.NAME, 'os_password')
    login.send_keys(os.getenv('LOGIN'))
    insert_pass.send_keys(os.getenv('PASS'))
    insert_pass.submit()

    browser.get('https://wiki.sptlab.ru/pages/viewpage.action?pageId=213025260')
    html = browser.page_source
    # with open("./page_source.html", "w", encoding='utf-8') as f:
    #     f.writelines(html)
    return html


def get_content():
    # with open("./page_source.html", "r", encoding='utf-8') as f:
    with open('page_source.html', 'r', encoding='utf-8') as f:
        html = f.read()
    datas = []
    i = 0
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('tbody')

    for tr in trs:
        date = {}
        date.clear()
        rows = tr.find_all('td', class_='confluenceTd')
        try:
            for _ in rows:
                # if rows[5].get_text(strip=True)  not in exclude_list:
                #     print(rows[2].get_text(strip=True))
                if rows[5].get_text(strip=True) not in exclude_list or rows[1].get_text(strip=True) != 'Отключен':
                    date['spp_name'] = rows[2].get_text(strip=True)
                    date['spp_inn'] = rows[4].get_text(strip=True)
                    date['spp_link'] = rows[7].find('a').get('href')
            if date:
                datas.append(date)

        except Exception as ex:
            print(ex)
            logging.info(ex)
            pass
    # print(datas)

    return datas


def save_to_db(date):
    conn = sqlite3.connect(r"E:\DB\sqlite\sqlite.db")
    cursor = conn.cursor()
    for i in range(0, len(date)):
        try:
            print('поптыка записи')
            sql = f"INSERT INTO spp VALUES(" \
                  f"'{date[i]['spp_name']}'," \
                  f" '{date[i]['spp_inn']}', '{date[i]['spp_link']}'," \
                  f" '{date[i]['spp_email']}', '{date[i]['spp_pass']}')"

            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            logging.info(ex)

    conn.close()


def save_to_scv(data):
    with open('./qwe.csv', 'w', encoding="UTF-8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['name', 'inn', 'link'])
        for item in data:
            writer.writerow([item['spp_name'], item['spp_inn'], item['spp_link']])


def main():
    # get_html(URL)
    get_content()
    # save_to_scv(get_content(get_html(URL)))
    # html = get_html(URL)
    # print(html)
    # print(get_content(html))
    # save_to_db(get_content(html))


if __name__ == '__main__':
    main()
