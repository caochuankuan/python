import requests
ret=requests.get('http://www.cqepc.cn')
print('HTTP状态码：',ret.status_code)
print('重庆航天职业技术学院主页内容是：',ret.text)
