ranges = []

with open('in/16.in') as fin:

    line = fin.readline().strip()
    while line != '':
        a, b = line.split()[-3::2]
        a = list(map(int, a.split('-')))
        a = range(a[0], a[1]+1)
        b = list(map(int, b.split('-')))
        b = range(b[0], b[1]+1)
        ranges.append(a)
        ranges.append(b)
        line = fin.readline().strip()
    
    for _ in range(4): fin.readline()

    res = 0
    for line in fin:
        for x in map(int, line.strip().split(',')):
            for r in ranges:
                if x in r:
                    break
            else:
                res += x
    
    print(res)
