import requests
from bs4 import BeautifulSoup
ret = requests.get("https://python123.io/ws/demo.html")
soup = BeautifulSoup(ret.text,'html.parser')
print(soup.prettify())
