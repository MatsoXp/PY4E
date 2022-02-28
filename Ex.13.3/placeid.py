#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps. 
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response. 
#Please run your program to find the place_id for this location:
#Saint Petersburg State University of Aerospace Instrumentation

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
