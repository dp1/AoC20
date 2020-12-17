def neighbours(x, y, z):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == 0 and j == 0 and k == 0: continue
                yield (x+i,y+j,z+k)

base = """.#.#.#..
..#....#
#####..#
#####..#
#####..#
###..#.#
#..##.##
#.#.####""".splitlines()

active = set()

for i in range(len(base)):
    for j in range(len(base)):
        if base[i][j] == '#':
            active.add((i,j,0))

for _ in range(6):
    counter = {}

    for u in active:
        for v in neighbours(*u):
            counter[v] = counter.get(v, 0) + 1
    
    new_active = set()
    for u in counter:
        if u in active and counter[u] in [2,3]:
            new_active.add(u)
        elif u not in active and counter[u] == 3:
            new_active.add(u)

    active = new_active
    

print(len(active))
