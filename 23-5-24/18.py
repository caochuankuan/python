import requests
from bs4 import BeautifulSoup
ret = requests.get('https://b.faloo.com/1305726_1.html')
ret.encoding = 'gbk'
bs=BeautifulSoup(ret.text)
texts = bs.find_all('div','p')
print(texts)
