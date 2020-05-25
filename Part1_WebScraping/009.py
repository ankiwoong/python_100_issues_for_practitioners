import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

links = soup.select('a')
print(len(links))
print('\n')

print(links[:3])
print('\n')

external_links = soup.select('a[class="external text"]')
print(external_links[:3])
print('\n')

id_selector = soup.select('#siteNotice')
print(id_selector)
print('\n')

id_selector2 = soup.select('div#siteNotice')
print(id_selector2)
print('\n')

id_selector3 = soup.select('p#siteNotice')
print(id_selector3)
print('\n')

class_selector = soup.select('.mw-headline')
print(class_selector)
print('\n')

class_selector2 = soup.select('span.mw-headline')
print(class_selector2)
