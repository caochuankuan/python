import requests
from bs4 import BeautifulSoup
ret = requests.get("http://www.cqepc.cn/index.html")
soup = BeautifulSoup(ret.text,'html.parser')
print(soup.body.contents)                     #获取body所有子节点元素列表
for child in soup.body.children:          #遍历body子节点元素
       print(child)
for child in soup.body.descendants:      #遍历body子孙节点元素
       print(child)
