import requests
from bs4 import BeautifulSoup
ret = requests.get("http://www.cqepc.cn/index.html")
soup = BeautifulSoup(ret.text,'html.parser')
print(soup.title.parent)
print(soup.html.parent)
for parent in soup.a.parents:
       if parent is None:
              print(parent)
       else:
              print(parent.name)