with open('in/2.in', 'r') as fin:
    lines = fin.readlines()

ctr = 0
for line in lines:
    a, b = map(int, line.split()[0].split('-'))
    ch = line.split()[1].split(':')[0]
    pw = line.split()[-1]

    if pw.count(ch) >= a and pw.count(ch) <= b:
        ctr += 1

print(ctr)
