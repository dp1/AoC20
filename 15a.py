start = [19,0,5,1,10,13]

# number -> turn
prev = {}
turn = 1

for x in start:
    prev[x] = turn
    turn += 1

last = start[-1]

while turn <= 2020:

    if last not in prev:
        num = 0
    else:
        num = turn - 1 - prev[last]
    
    prev[last] = turn - 1
    last = num

    turn += 1

print(last)
