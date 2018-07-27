csvraw = open("n1file.csv", "r")
stamps = open("n2file.csv", "r")
file = open("combine.tsv","w")
fileone = 'n1'
filetwo = 'n2'
file.write(fileone+"	"+filetwo+"\n")
for line in csvraw:
    file.write(line.rstrip()+"	"+stamps.readline().strip()+"\n")
file.close()
