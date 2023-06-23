from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dataclasses import dataclass

UA = UserAgent(fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')

HEADERS = {"User-Agent": UA.random}
SEARCH_URL = "https://google.ru"


@dataclass
class GetExtend:
    res_extend_link: list

    def get_message(self):
        print(f"Запросы, связанные с вашим:\n")
        for i in range(len(self.res_extend_link)):
            print(self.res_extend_link[i])


class GoogleExtend:
    def __init__(self, html):
        self.html = html

    def get_content(self):
        i = 0
        soup = BeautifulSoup(self.html, "lxml")
        txt = soup.find(text="Связанные запросы").parent
        res = txt.find_next("div").find_all("a")
        extends_link = []
        for _ in res:
            try:
                link_extend_text = res[i].get_text()
                link_extend = "https://www.google.ru" + res[i].get("href")
                i += 1
                extends_link.append(link_extend_text + " " + link_extend)
            except:
                print("Нема дополнительных ссылок")

        return extends_link

    def info_mess(self) -> GetExtend:
        return GetExtend(self.get_content())


def get_page(search_str):

    s = Service("./chromedriver.exe")
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    browser = webdriver.Chrome(service=s, options=options)
    browser.get(SEARCH_URL)
    search_string = browser.find_element(By.NAME, "q")
    search_string.send_keys(search_str)
    search_string.submit()
    html_sourse = browser.page_source
    return GoogleExtend(html_sourse)


def main(what):
    info = GoogleExtend.info_mess(what)
    return info.get_message()


if __name__ == "__main__":
    s_str: str = input()
    what = get_page(s_str)
    main(what)
