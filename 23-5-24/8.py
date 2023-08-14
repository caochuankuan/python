import requests
from bs4 import BeautifulSoup
ret = requests.get("http://www.cqepc.cn/index.html ")
soup = BeautifulSoup(ret.text,'html.parser')
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
for sibling in soup.a.next_sibling:
    print(sibling)
for sibling in soup.a.previous_sibling:
      print(sibling)
