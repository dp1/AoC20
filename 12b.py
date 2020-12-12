with open('in/12.in', 'r') as fin:
    code = [x.strip() for x in fin.readlines()]

pos = [0,0]
waypoint = [-1,10]

for instr in code:
    action, value = instr[0], int(instr[1:])

    if action == 'N': waypoint[0] -= value
    elif action == 'S': waypoint[0] += value
    elif action == 'E': waypoint[1] += value
    elif action == 'W': waypoint[1] -= value
    elif action == 'L':
        for _ in range(value//90):
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif action == 'R':
        for _ in range(value//90):
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    elif action == 'F':
        pos[0] += waypoint[0] * value
        pos[1] += waypoint[1] * value

print(abs(pos[0]) + abs(pos[1]))
