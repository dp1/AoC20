with open('8.in', 'r') as fin:
    code = [x.strip() for x in fin.readlines()]

visited = set()

pc = 0
acc = 0
while True:
    if pc in visited:
        print(acc)
        break
    visited.add(pc)
    
    instr = code[pc]

    opcode, arg = instr.split()
    arg = int(arg)

    if opcode == 'nop': pass
    elif opcode == 'acc': acc += arg
    else: pc += arg-1

    pc += 1
