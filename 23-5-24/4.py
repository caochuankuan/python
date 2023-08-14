import requests
key ={'Word':'Italia','alex':'utf-8'}
ret =requests.request('GET','https://www.baidu.com/s',params=key)
print(ret.url)
