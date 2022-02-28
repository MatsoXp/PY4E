#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1494601.txt (There are 101 values and the sum ends with 837)
#These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis. 

import re

userFile = "regex_sum_1494601.txt"
userFile = open(userFile)

counter = 0
numList = []
for line in userFile:
    line = re.findall('[0-9]+', line)
    if len(line) < 1: 
        continue
    for number in line:
        intNumber = int(number)
        numList.append(intNumber)
        counter = counter + 1

print('Total sum',sum(numList))
print('Found',counter, 'numbers')
