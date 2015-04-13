import requests
url = 'http://www.google.com'
r = requests.get(url)
binary = r.content
converted = binary.decode('utf-8')
data = r.text
print(data)
print(data == converted)
print(r.status_code)
print(r.history)

from urllib.parse import urlencode

data = {'status': 'Test update from Python 3'}
encoded = urlencode(data)
print(encoded)
