import urllib.error, urllib.request, urllib.parse
import json

api = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location: ')
url = api + urllib.parse.urlencode({'address': address, 'key' : 42})

data = urllib.request.urlopen(url).read()
js = json.loads(data)

print('Retrieving', url)
print('Retrived', len(data), 'characters')
print('Place id', js['results'][0]['place_id'])
