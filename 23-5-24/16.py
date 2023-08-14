import requests
import re
from bs4 import BeautifulSoup
ret = requests.get('http://www.cqepc.cn/index.html')
ret.encoding = 'gb2312'
uhtext = ret.text
soup = BeautifulSoup(uhtext,'html.parser')
soup.find_all(text=re.compile("重庆"),limit=4)
