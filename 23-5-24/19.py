import requests
from bs4 import BeautifulSoup
ret = requests.get('http://www.mbiqukan.com/911/911335/1.html')
ret.encoding = 'gb2312'
bs=BeautifulSoup(ret.text)
texts = bs.find_all('div',class_ = 'showtxt')
print(texts)