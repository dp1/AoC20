with open('in/6.in', 'r') as fin:
    groups = [x.split('\n') for x in fin.read().split('\n\n')]

res = 0
for group in groups:
    letters = set()
    for answer in group:
        letters = letters.union(set(answer))
    res += len(letters)

print(res)
