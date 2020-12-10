val = []
for line in open('in/5.in', 'r').readlines():
    line = line.strip()
    line = line.replace('F', '0').replace('B', '1')
    line = line.replace('L', '0').replace('R', '1')
    val.append(int(line, 2))

val = set(val)
for x in range(min(val)+1, max(val)):
    if x not in val:
        print(x)
