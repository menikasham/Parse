# -*- coding: utf-8 -*-

from auth_adm import pref
import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import logging
import sqlite3

logging.basicConfig(
    filename="adm_parse.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s",
)

ua = UserAgent()

URL = "adm_all.mcdn.codes/"
HEADERS = {"User-Agent": ua.random}
FILE = r"c:\SPT\adm_all.csv"


def get_html(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument(HEADERS["User-Agent"])
    s = Service(r"C:\Terminal\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.get(f'https://{pref["login"]}:{pref["pass"]}@{URL}')
    html = browser.page_source
    return html


def get_content(html):
    i = 0
    soup = BeautifulSoup(html, "lxml")
    print_houses = []
    table = soup.findChildren("table")
    my_table = table[0]
    rows = my_table.find_all("tr")

    for _ in range(len(rows)):

        if not rows[i].find("td").get_text():
            i += 1
            continue
        else:
            print_houses.append(
                {
                    "name": rows[i].find("td").get_text(),
                    "webid": rows[i].find("a").get_text(),
                    "webid_link": rows[i].find("a").get("href"),
                    "link_adm": rows[i].find("a").get("href").split("//")[0]
                    + "//adm_"
                    + rows[i].find("a").get("href").split("//")[1],
                }
            )
            i += 1

    return print_houses


def insert_into_db(dictionary):
    conn = sqlite3.connect(r"D:\DB\sqlite.db")
    cursor = conn.cursor()
    for i in range(0, len(dictionary)):
        try:
            sql = (
                f"INSERT INTO Customers (web_id_link, adm_link) VALUES("
                f"'{dictionary[i]['webid_link']}','{dictionary[i]['link_adm']}') "
                f"where webID='{dictionary[i]['webid']}';"
            )

            cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            logging.info(ex)

    conn.close()


def save_result(items, path):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Название", "WebID", "WebID Link", "ADM Link"])
        for item in items:
            writer.writerow(
                [item["name"], item["webid"], item["webid_link"], item["link_adm"]]
            )


def main():
    html = get_html(URL)
    # save_result(get_content(html), FILE)
    insert_into_db(get_content(html))


if __name__ == "__main__":
    main()
