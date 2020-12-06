with open('3.in', 'r') as fin:
    grid = [x.strip() for x in fin.readlines()]

res = 1
for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    x, y, ctr = 0, 0, 0
    while y < len(grid) - 1:
        y += slope[1]
        x = (x+slope[0]) % len(grid[0])
        if y < len(grid) and grid[y][x] == '#':
            ctr += 1
    
    res *= ctr

print(res)
