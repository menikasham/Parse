from bs4 import BeautifulSoup as bs
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

base_url = "https://en.soccerwiki.org/league.php?leagueid=28"


with open('./soccer.html', 'r') as soccer:

  soup = bs(soccer, 'lxml')
  # print(soup.prettify())
  div = soup.find_all('div', class_='table-custom-responsive')[0]
  table = div.find_next('table', attrs={'class': ['table-custom', ' table-roster']})
  tr_s = table.find_all('tr')

  for _ in range(len(tr_s)):
    name = tr_s[5].find('td').get_text(),
    print(name)



# .find('table', class_='table-roster')



# html = requests.get(base_url, headers=HEADERS).text
# with open('./soccer.html', 'w', encoding="utf-8") as output_file:
#     output_file.write(html)




# soup = bs(html, 'lxml')
# div = soup.find_all('div', class_='factfileBorder')[1]
# table = div.find_next('table', attrs={'class':['tabledata', 'no-arrow']})
# td_s = table.select('td.team:nth-child(2)')
# print('-*'*10)
# for td in td_s:
#     print(td.find('a').text)


# if __name__ == "__main__":
#     pass

