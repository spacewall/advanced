import requests
import os
import lxml
from pprint import pprint
from bs4 import BeautifulSoup

def find_tags():
    vacations = dict()
    
    for page in range(len(os.listdir("pages"))):
        with open(f"pages/page_{page}.html") as page:
            src = page.read()

        soup = BeautifulSoup(src, "lxml")

        blocks = soup.find("body").find("div", id="HH-React-Root").find_all("div", class_="vacancy-serp-item-body")

        for block in blocks:
            name_href = block.find("a", class_="serp-item__title")
            print(name_href)

def main(url, headers):
    if "pages" not in os.listdir():
        os.mkdir("pages")

    if os.listdir("pages") == []:
        for page in range(40):
            responce = requests.get(url + f"&page={page}", headers=headers)

            with open(f"pages/page_{page}.html", "w") as main_page:
                main_page.write(responce.text)

            print(f"Page {page} has been successfully created!")

    find_tags()

if __name__ == "__main__":
    url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2562 Yowser/2.5 Safari/537.36"
    }
    
    main(url, headers)