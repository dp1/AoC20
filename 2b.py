with open('2.in', 'r') as fin:
    lines = fin.readlines()

ctr = 0
for line in lines:
    a, b = map(int, line.split()[0].split('-'))
    ch = line.split()[1].split(':')[0]
    pw = line.split()[-1]

    if (pw[a-1] == ch) != (pw[b-1] == ch):
        ctr += 1

print(ctr)
