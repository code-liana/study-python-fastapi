import requests
#
# x = requests.get('https://w3schools.com/python/demopage.htm')
#
# print(x.text)
# print(x.headers)

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url=url, json = myobj)

print(x)
print(x.headers)
print(x.status_code)
print(x.content)
print(x.reason)