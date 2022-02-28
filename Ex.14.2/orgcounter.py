#This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
#CREATE TABLE Counts (org TEXT, count INTEGER)
#You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
#The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt. 

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input("Type the file name: ")

try:
    fhandle = open(fname)
except:
    print("File does not exist!", fname)
    quit()

for line in fhandle:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    address = email.find('@')
    org = email[address+1:len(email)]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count)VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()