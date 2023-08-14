import requests
def getHTMLText(url):
       try:
              r = requests.get(url,timeout=30)
              r.raise_for_status()
              print(r.apparent_encoding)
              r.encoding = r.apparent_encoding
              return r.text
       except:
              return "产生异常"
print(getHTMLText('http://www.google.com'))#Google无法访问，输出产生异常
print(getHTMLText('http://www.baidu.com')) #Baidu正常访问，输出内容
