#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.#

fname = input("Type the file name: ")

try:
    fhandle = open(fname)
except:
    print("File does not exist!", fname)
    quit()

total = 0
foundLines = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        numberPosition = line.find(':')
        number = float(line[numberPosition + 1 : ])
        total = total + number
        foundLines = foundLines + 1

print("Average spam confidence:", total / foundLines)
