import requests
from bs4 import BeautifulSoup
import csv


item = "애플워치"
URL = f"https://www.daangn.com/search/{item}"


result = requests.get(URL)
soup = BeautifulSoup(result.text, 'html.parser')

section = soup.find("div", {"class": "articles-wrap"})

extract_card = section.find_all(
    "article", {"class": "flea-market-article flat-card"})

title = []


for x in extract_card:
    a = x.find("span", {"class": "article-title"}).string.strip()
    b = x.find("p", {"class": "article-region-name"}).string.strip()
    img = x.find("img")["src"]
    c = a, b, img
    title.append(c)


def save_csv(item):
    file = open("ex.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "location", "image-link"])
    for i in item:
        writer.writerow(i)
    return


save_csv(title)
