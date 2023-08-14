import requests
from bs4 import BeautifulSoup
ret = requests.get('http://www.cqepc.cn/index.html')
uhtext = ret.text
soup = BeautifulSoup(uhtext,'html.parser')
print(soup.prettify())
