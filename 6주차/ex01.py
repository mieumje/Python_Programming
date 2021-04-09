import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.daangn.com/hot_articles"

result = requests.get(URL)
soup = BeautifulSoup(result.text, 'html.parser')

card = soup.find_all("div", {"class": "card-desc"})

""" section = soup.find("section", {"class": "cards-wrap"}) """
#titles = soup.find_all("h2", {"class": "card-title"})


article = []
for i in card:
    titles = i.find("h2", {"class": "card-title"}).string
    prices = i.find("div", {"class": "card-price"}).string.strip()
    locations = i.find("div", {"class": "card-region-name"}).string.strip()
    a = titles, prices, locations
    article.append(a)


def save_csv(item):
    file = open("articles.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["상품", "가격", "위치"])
    for i in item:
        writer.writerow(i)
    return


save_csv(article)
