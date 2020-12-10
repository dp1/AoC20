import string

with open('in/7.in', 'r') as fin:
    lines = [x.strip() for x in fin.readlines()]

graph = {}

for line in lines:
    if len(line) == 0: continue

    outer = line.split(' bags')[0]
    if outer not in graph: graph[outer] = []
    if 'no other bags' in line: continue

    line = line.split('contain ')[1]
    for chunk in line.split('bag'):

        while len(chunk) > 0 and chunk[0] not in string.digits:
            chunk = chunk[1:]
        if len(chunk) == 0: continue

        ctr, inner = chunk.split(' ', 1)
        ctr, inner = int(ctr), inner.strip()

        if inner not in graph: graph[inner] = []
        graph[outer].append((inner, ctr))

memo = {}

def f(u):
    global memo
    if u in memo: return memo[u]
    memo[u] = 1

    for (v,ctr) in graph[u]:
        memo[u] += ctr * f(v)
    
    return memo[u]

print(f('shiny gold') - 1)
