fname = input("Type the file name: ")

try:
    fhandle = open(fname)
except:
    print("File does not exist!", fname)
    quit()

adressCounter = dict()
for line in fhandle:
    if line.startswith('From '):
        lineSplit = line.split()
        adress = lineSplit[1]
        adressCounter[adress] = adressCounter.get(adress, 0) + 1

userMail = None
mailCounter = None
for k, v in adressCounter.items():
    if mailCounter is None or mailCounter < v:
        userMail = k
        mailCounter = v
        
print(userMail, mailCounter)