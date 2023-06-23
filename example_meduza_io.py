from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request
import requests
import time

UA = UserAgent(fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')

HEADERS = {"User-Agent": UA.random}
SEARCH_URL = "https://www.lifetime.plus"
meduza = "https://meduza.io"


def get_page():
    s = Service(r"C:\Terminal\chromedriver.exe")
    driver = Chrome(service=s)
    driver.get(meduza)
    time.sleep(5)


def get_image(element):
    images_element = element.find_element(By.CLASS_NAME, "ImageElement-root")
    image_element = images_element.find_element(By.TAG_NAME, "source")

    return "https://meduza.io" + image_element.get_attribute("srcset").strip()


def get_title(element):
    title_element = element.find_element(By.CLASS_NAME, "Link-root")
    return title_element.text


def get_date(element):
    date_element = element.find_element(By.CLASS_NAME, "Timestamp-module_root__coOvT")

    return date_element.text


def get_news():
    news = []
    news_elements = driver.find_elements(By.CLASS_NAME, "categories-0-2-530")

    for element in news_elements:
        print(element)
        data = {
          "image": get_image(element),
          "title": get_title(element),
          "date": get_date(element),
        }
        news.append(data)

    return news

def print_data_news():
    news_items = get_news()

    for news in news_items:
        print(f"""
        Изображение: {news['image']}
        Заголовок: {news['title']}
        Дата создание: {news['date']}
        """)

if __name__ == "__main__":
    s = Service(r"C:\Terminal\chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = Chrome(service=s, options=options)
    driver.get("https://www.lifetime.plus/")
    print_data_news()

