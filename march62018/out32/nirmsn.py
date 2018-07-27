with open('n1.txt', 'r') as t1, open('n2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
    for line in filetwo:
	for line1 in fileone:
            if line not in line1:
		print(line1,line)
