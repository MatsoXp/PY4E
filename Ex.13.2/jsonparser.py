#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1494606.json (Sum ends with 26)

import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location:')
urllink = urllib.request.urlopen(address)
data = urllink.read()

info = json.loads(data)

total = 0
count = 0
for item in info['comments']:
    rawNumber = int(item['count'])
    count = count + 1
    total = total + rawNumber

print('Retrieved:',len(data),'characters')
print('Retrieved:',count,'numbers')
print('Total sum:',total)
