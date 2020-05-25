import requests

url = "https://www.python.org/"
resp = requests.get(url)

html = resp.text
print(html)
