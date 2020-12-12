with open('in/12.in', 'r') as fin:
    code = [x.strip() for x in fin.readlines()]

pos = [0,0]
angle = 0

for instr in code:
    action, value = instr[0], int(instr[1:])

    if action == 'N': pos[0] -= value
    elif action == 'S': pos[0] += value
    elif action == 'E': pos[1] += value
    elif action == 'W': pos[1] -= value
    elif action == 'L': angle = (angle + value//90) % 4
    elif action == 'R': angle = (angle - value//90 + 4) % 4
    elif action == 'F':
        mapping = {
            0: (0, 1),
            1: (-1, 0),
            2: (0, -1),
            3: (1, 0)
        }
        pos[0] += mapping[angle][0] * value
        pos[1] += mapping[angle][1] * value

print(abs(pos[0]) + abs(pos[1]))
