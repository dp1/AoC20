start = [19,0,5,1,10,13]

# number -> turn
prev = [-1] * 30000001

for turn,x in enumerate(start):
    prev[x] = turn + 1

last = start[-1]

for turn in range(len(start)+1, 30000001):

    ctr = prev[last]
    if ctr == -1:
        num = 0
    else:
        num = turn - 1 - ctr
    
    prev[last] = turn - 1
    last = num

print(last)
