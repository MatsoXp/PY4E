#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Type the file name: ")

try:
    fhandle = open(fname)
except:
    print("File does not exist!", fname)
    quit()

storeWords = list()
for line in fhandle:
    lineSplit = line.split()
    for word in lineSplit:
        if word in storeWords:
            continue
        storeWords.append(word)

storeWords.sort()
print(storeWords)