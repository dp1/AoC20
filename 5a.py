res = 0
for line in open('5.in', 'r').readlines():
    line = line.strip()
    line = line.replace('F', '0').replace('B', '1')
    line = line.replace('L', '0').replace('R', '1')
    res = max(res, int(line, 2))

print(res)
