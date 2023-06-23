import datetime

import psycopg2
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from psycopg2 import Error

start_time = datetime.datetime.now()

UA = UserAgent()
HEADERS = {"User-Agent": UA.random}
BASE_URL = "https://run365.ru/"

dict_content = {
    "man": "Мужчинам",
    "woman": "Женщинам",
    "kid": "Детям",
    "accs": "Аксессуары",
}


def write_to_db(store_list: list):
    # поправил вроде. также можно весь массив за раз передавать
    # но еще не разобрался толком ((

    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Seamni31",
            host="127.0.0.1",
            port="5432",
            database="postgres",
        )
        cursor = connection.cursor()
        for i in range(len(store_list)):
            # для этого проекта делать строку запроса прям на месте ок. В боевых системах все данные,
            # поступающие в БД сначала должны быть валидированы и все символы экранированы.
            insert_query = (
                f"INSERT INTO store365 (model_name, price,"
                f" sale_price, sale_percent, size, model_link)"
                f' VALUES (\'{store_list[i]["model_name"]}\','
                f' \'{store_list[i]["price"]}\','
                f' \'{store_list[i]["sale_price"]}\','
                f' \'{store_list[i]["sale_percent"]}\','
                f' \'{store_list[i]["size"]}\','
                f' \'{store_list[i]["model_link"]}\')'
            )
            cursor.execute(insert_query)
            connection.commit()
        connection.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    # тоже поправил) забыл про это


def get_number_pages(page):
    soup = BeautifulSoup(
        requests.get(page, headers={"User-Agent": UA.random}).text, "lxml"
    )
    try:
        pages = soup.find("ul", class_="page-numbers").find_all(
            "a", class_="page-numbers"
        )
        pages = int(pages[-2].text)
    except:
        pages = 1

    return pages


def get_content():
    # а эту функцию хочется разбить на части, т.к. читать в таком виде ее тяжело
    # вероятно, красивее бы выглядил ее рекурсивный вариант, но это не точно :)
    for key in dict_content:

        soup = BeautifulSoup(
            requests.get(BASE_URL, headers={"User-Agent": UA.random}).text, "lxml"
        )
        list_links = []
        all_cat = soup.find("a", string=dict_content[key]).parent
        all_links = all_cat.select('a[href^="https://run365.ru/"]')
        for item in all_links:
            list_links.append(str(item).split('"')[1])

        for link in list_links:
            model = []
            count_p = get_number_pages(link)
            for i in range(1, count_p + 1):

                link_p = link + "page/" + str(i)
                soup = BeautifulSoup(
                    requests.get(link_p, headers={"User-Agent": UA.random}).text, "lxml"
                )
                content = soup.find("div", class_="content").find_all(
                    "div", class_="product-container"
                )

                for i in range(len(content)):
                    model_name = content[i].find("h2").text
                    model_link = content[i].find("a").get("href")
                    price = (
                        content[i]
                        .find("div", class_="price")
                        .get_text(strip=True)
                        .split(" ")[0]
                    )
                    sale_price = None
                    sale_percent = None
                    size = None

                    if content[i].find("div", class_="box-sizes"):
                        size = (
                            content[i]
                            .find("div", class_="box-sizes")
                            .get_text(strip=True)
                        )

                    if content[i].find("div", class_="price-sale"):
                        sale_price = (
                            content[i]
                            .find("div", class_="price-sale")
                            .text.split(" ")[0]
                        )
                        sale_percent = (
                            content[i]
                            .find("div", class_="price")
                            .get_text(strip=True)
                            .split("-")[1][:2]
                        )

                    model.append(
                        {
                            "model_name": model_name,
                            "price": price,
                            "sale_price": sale_price,
                            "sale_percent": sale_percent,
                            "size": size,
                            "model_link": model_link,
                        }
                    )
            print("Пишем в БД")
            write_to_db(model)


def main():
    get_content()
    finish_time = datetime.datetime.now()
    total_time = finish_time - start_time
    print(f"Заняло времени: {total_time.total_seconds()}")


if __name__ == "__main__":
    BASE_URL = "https://run365.ru/"
    main()
