with open('in/10.in', 'r') as fin:
    data = sorted([int(x) for x in fin.readlines()])

cur = 0
ctr = {x:0 for x in range(4)}

for x in data:
    delta = x - cur
    ctr[delta] += 1
    cur = x

ctr[3] += 1

print(ctr[1] * ctr[3])
