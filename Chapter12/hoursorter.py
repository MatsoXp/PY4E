#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Type the file name: ")

try:
    fhandle = open(fname)
except:
    print("File does not exist!", fname)
    quit()

timeDict = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        time = time[0:2]
        timeDict[time] = timeDict.get(time, 0) + 1

timeList = list()
for k, v in timeDict.items():
    timeList.append((k, v))

timeList.sort()
for k,v in timeList:
    print(k, v)