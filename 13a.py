with open('in/13.in') as fin:
    T = int(fin.readline())
    V = [int(x) for x in fin.readline().strip().split(',') if x != 'x']

best = None
res = 0
for x in V:
    wait = x - T % x
    if not best or wait < best:
        best = wait
        res = x * wait

print(res)
