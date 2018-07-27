import csv
with open('n1.txt', 'rb') as wn:
    reader = csv.reader(wn)
    winningnumbers = list(reader)

with open('n1.txt', 'rb') as en:
    readere = csv.reader(en)
    for line_index, line in enumerate(readere):
        if all((line[i] == winningnumbers[i] for i in xrange(len(line)))):
            winning_number_index = line_index
            break
    else:
        winning_number_index = -1

print(winning_number_index)
