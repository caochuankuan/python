import requests
from bs4 import BeautifulSoup
ret = requests.get("https://www.xbqgyy.com/book/24476/5897925.html")
ret.encoding = "utf-8"
print(ret.text)