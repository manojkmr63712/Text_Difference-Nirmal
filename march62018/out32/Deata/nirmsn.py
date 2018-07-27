import sys
import difflib
from difflib import SequenceMatcher
with open('n1.txt', 'r') as t1, open('n2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
    #fileout = open("combine.txt","w")
    for line in filetwo:
	for line1 in fileone:
            if line not in line1:
		s = SequenceMatcher(lambda x: x == " ",line1,line)
		#print(round(s.ratio(),3))
		if (round(s.ratio(),3)) >= 0.9:
		    result = difflib.ndiff(line1.splitlines(),line.splitlines())
		    #fileout.write('\n'.join(result))
		    print('\n'.join(result))
    #fileout.close()
