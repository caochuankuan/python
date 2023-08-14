import requests
from bs4 import BeautifulSoup
ret = requests.get('http://www.cqepc.cn/index.html')
ret.encoding = 'gb2312'
uhtext = ret.text
soup = BeautifulSoup(uhtext,'html.parser')
print(soup.select('#sub_09'))
print(soup.select('#sub_01'))
print(soup.prettify())
