import requests
from bs4 import BeautifulSoup
ret = requests.get("https://www.xbqgyy.com/book/24476/5897925.html")
ret.encoding = "utf-8"
bs = BeautifulSoup(ret.text)
texts = bs.find_all("article",class_ = "content")
print(texts)