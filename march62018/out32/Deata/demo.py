import sys
import difflib
from difflib import SequenceMatcher
inputfile_one = sys.argv[1]
inputfile_two = sys.argv[2]
output_file = sys.argv[3]
with open(inputfile_one, 'r') as t1, open(inputfile_two, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
    fileout = open(output_file,"w")
    for line in filetwo:
	dataone = line
	dataone = dataone.replace('\n','')
	for line1 in fileone:
	    datatwo = line1
	    datatwo = datatwo.replace('\n','')
            if line not in line1:
		s = SequenceMatcher(lambda x: x == " ",line1,line)
		if (round(s.ratio(),3)) >= 0.9:
		    result = line1,line
		    fileout.write(str(id(result))+"|"+dataone+"|"+datatwo+'\n')
    fileout.close()
