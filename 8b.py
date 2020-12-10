with open('in/8.in', 'r') as fin:
    code = [x.strip() for x in fin.readlines()]

def simulate(code):
    visited = set()

    pc = 0
    acc = 0
    while True:
        if pc in visited:
            return (False, acc)
        if pc >= len(code):
            break
        
        visited.add(pc)

        instr = code[pc]

        opcode, arg = instr.split()
        arg = int(arg)

        if opcode == 'nop': pass
        elif opcode == 'acc': acc += arg
        else: pc += arg-1

        pc += 1
    
    return (True, acc)

for i in range(len(code)):
    if code[i][:3] == 'acc': continue
    
    if code[i][:3] == 'nop':
        edit = 'jmp' + code[i][3:]
    else:
        edit = 'nop' + code[i][3:]

    newcode = code[:i] + [edit] + code[i+1:]

    res = simulate(newcode)
    if res[0]:
        print(res[1])
