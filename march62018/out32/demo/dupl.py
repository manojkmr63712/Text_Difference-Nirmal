import os
import re

def extract_addr(fin, fout, phone_pattern):
    global cnt
    for line in fin:
	line = line.strip()
    	m = re.search(phone_pattern, line)
    	addr = None
    	if m is None:
      	    addr = line
    	else:
      	    start = m.start()
      	    addr = line[0:start].strip()
    	fout.write("%d %s\n" % (cnt, addr))
    	cnt += 1

orig_dir = "original"
proc_dir = "data"

input_files = ["n1.txt", "n2.csv"]
phone_patterns = [r"\d{3}\/", r"\d{3}-"]
fout = open(os.path.join(proc_dir, "addresses.txt"), 'wb')
cnt = 1
for i in range(0, 2):
    input_file = input_files[i]
    phone_pattern = phone_patterns[i]
    fin = open(os.path.join(orig_dir, input_file), 'rb')
    extract_addr(fin, fout, phone_pattern)
    fin.close()
fout.close()
