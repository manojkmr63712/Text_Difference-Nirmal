import csv
with open('n1.txt', 'r') as t1, open('n2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
    file1 = open("n2file.csv","w")
    for line in filetwo:
        if line not in fileone:
	    file1.write(line)
    file1.close()
    file2 = open("n1file.csv","w")
    for line in fileone:
        if line not in filetwo:
            file2.write(line)
    file2.close()
