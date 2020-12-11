def near(grid, i, j):
    ctr = 0
    for (a,b) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        if i+a >= 0 and j+b >= 0 and i+a < len(grid) and j+b < len(grid[0]):
            if grid[i+a][j+b] == '#':
                ctr += 1
    return ctr

def step(grid):
    newgrid = [['' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    changed = False

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == '.':
                newgrid[i][j] = '.'

            elif grid[i][j] == 'L':
                if near(grid, i, j) == 0:
                    newgrid[i][j] = '#'
                    changed = True
                else:
                    newgrid[i][j] = 'L'

            elif grid[i][j] == '#':
                if near(grid, i, j) >= 4:
                    newgrid[i][j] = 'L'
                    changed = True
                else:
                    newgrid[i][j] = '#'

            else:
                print('error')
                exit(1)
    
    return changed, newgrid


with open('in/11.in', 'r') as fin:
    grid = [list(x.strip()) for x in fin.readlines()]

changed = True
while changed:
    changed, grid = step(grid)

res = sum(x.count('#') for x in grid)
print(res)
