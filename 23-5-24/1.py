import requests
ret=requests.get('http://www.cqepc.cn')
print('HTTP状态码：',ret.status_code)
print('重庆航天职业技术学院主页内容是：',ret.text)
print('猜测的响应内容编码方式为：',ret.encoding)
print('分析出响应内容的编码方式为：',ret.apparent_encoding)
print('响应内容的二进制形式为:',ret.content)
print('头部信息集合为',ret.headers)
