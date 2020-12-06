with open('6.in', 'r') as fin:
    groups = [x.split('\n') for x in fin.read().split('\n\n')]

res = 0
for group in groups:
    ctr = {}
    for answer in group:
        for ch in answer:
            if ch not in ctr: ctr[ch] = 0
            ctr[ch] += 1
    
    for ch in ctr:
        if ctr[ch] == len(group):
            res += 1

print(res)
