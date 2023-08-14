import requests
from bs4 import BeautifulSoup
ret = requests.get("https://www.xbqgyy.com/book/24476/5897925.html")
ret.encoding = "UTF-8"
bs = BeautifulSoup(ret.text)
texts = bs.find_all("article",class_ = "content")
text = texts[0].text.replace("</p>","\n").replace("<p>","")
myfile = open("G:\\python\\23-5-30\\aaa.txt","a")
myfile.write(text)
myfile.close()