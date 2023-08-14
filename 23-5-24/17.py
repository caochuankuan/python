import requests
from bs4 import BeautifulSoup
ret = requests.get('https://b.faloo.com/1305726_1.html')
ret.encoding = 'gbk'
print(ret.text)