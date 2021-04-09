import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

URL = "https://www.daangn.com/hot_articles"

result = requests.get(URL)
soup = BeautifulSoup(result.text, 'html.parser')

card = soup.find_all("div", {"class": "card-desc"})

""" section = soup.find("section", {"class": "cards-wrap"}) """
#titles = soup.find_all("h2", {"class": "card-title"})


article = []
t = []
p = []
l = []
for i in card:
    titles = i.find("h2", {"class": "card-title"}).string
    prices = i.find("div", {"class": "card-price"}).string.strip()
    locations = i.find("div", {"class": "card-region-name"}).string.strip()
    t.append(titles)
    p.append(prices)
    l.append(locations)

    #a = titles, prices, locations
    # article.append(a)

write_wb = Workbook()

write_ws = write_wb.active
write_ws['A1'] = '상품'
write_ws['B1'] = '가격'
write_ws['C1'] = '위치'


for i in range(0, len(card)):
    write_ws.append([t[i], p[i], l[i]])

write_wb.save('C:/Users/82105/Desktop/파이썬 프로그래밍/Python_Programming/당근.xlsx')

""" def save_csv(item):
    file = open("articles.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["상품", "가격", "위치"])
    for i in item:
        writer.writerow(i)
    return


save_csv(article) """
