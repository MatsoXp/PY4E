#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1494605.xml (Sum ends with 98)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

userUrl = input('Enter URL: ')
url = urllib.request.urlopen(userUrl)
data = url.read()

data = ET.fromstring(data)
numbers = data.findall('comments/comment/count')

sum = 0
count = 0
for number in numbers:
    sum = sum + int(number.text)
    count += 1

print('Count:', count)
print(sum)
