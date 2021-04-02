import urllib.request as req
from bs4 import BeautifulSoup

res = req.urlopen('https://daum.net')
html = res.read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('img')
for tag in tags:
    print(tag.get('src', None))
