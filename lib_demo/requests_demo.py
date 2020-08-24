import requests

r1 = requests.get('http://www.baidu.com')
r2 = requests.get('http://www.baidu.com', params={'param1':'value1'})
print(r1)