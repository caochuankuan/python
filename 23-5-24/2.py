import requests
ret=requests.get('http://www.google.com')
print('HTTP状态码：',ret.status_code)
print('google的内容是：',ret.text)
