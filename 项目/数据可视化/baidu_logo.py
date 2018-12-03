import requests
url = 'http://www.baidu.com/img/bd_logo1.png?qua=high&where=super'

req = requests.get(url)

with open('baidu_logo.png', 'wb') as f:
    f.write(req.content)

print(req.text)
