from auth import pref
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import logging
import sqlite3


logging.basicConfig(
    filename="wiki_parse.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s",
)

ua = UserAgent()

URL = "https://wiki.sptlab.ru/login.action?os_destination=%2F"
HEADERS = {"User-Agent": ua.random}


def get_html(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument(HEADERS["User-Agent"])
    s = Service(r"C:\Terminal\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.get(URL)

    login = browser.find_element(By.NAME, "os_username")
    insert_pass = browser.find_element(By.NAME, "os_password")
    login.send_keys(pref["login"])
    insert_pass.send_keys(pref["pass"])
    insert_pass.submit()

    browser.get("https://wiki.sptlab.ru/pages/viewpage.action?pageId=213025260")
    html = browser.page_source
    return html


def get_content(html):
    datas = []
    i = 0
    soup = BeautifulSoup(html, "lxml")
    trs = soup.find("table", class_="fixed-table").find_all("tr")

    for tr in trs:
        date = {}
        date.clear()
        rows = tr.find_all("td", class_="confluenceTd")
        try:
            for _ in rows:
                date["spp_name"] = rows[1].get_text(strip=True)
                date["spp_inn"] = rows[3].get_text(strip=True)
                date["spp_link"] = rows[7].find("a").get("href")
                date["spp_email"] = rows[8].get_text(strip=True)
                date["spp_pass"] = rows[9].get_text(strip=True)
            if date:
                datas.append(date)
        except Exception as ex:
            print(ex)
            logging.info(ex)
            pass

    return datas


def save_to_db(date):
    conn = sqlite3.connect(r"E:\DB\sqlite\sqlite.db")
    cursor = conn.cursor()
    for i in range(0, len(date)):
        try:
            print("поптыка записи")
            sql = (
                f"INSERT INTO spp VALUES("
                f"'{date[i]['spp_name']}',"
                f" '{date[i]['spp_inn']}', '{date[i]['spp_link']}',"
                f" '{date[i]['spp_email']}', '{date[i]['spp_pass']}')"
            )

            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            logging.info(ex)

    conn.close()


def main():
    html = get_html(URL)
    print(get_content(html))
    # save_to_db(get_content(html))


if __name__ == "__main__":
    main()
