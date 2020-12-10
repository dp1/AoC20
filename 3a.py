with open('in/3.in', 'r') as fin:
    grid = [x.strip() for x in fin.readlines()]

x, y, ctr = 0, 0, 0

while y < len(grid) - 1:
    y += 1
    x = (x+3) % len(grid[0])
    if grid[y][x] == '#':
        ctr += 1

print(ctr)
