with open('in/14.in') as fin:
    lines = [x.strip() for x in fin.readlines()]

mem = {}
mask1, mask0 = 0, 0

for line in lines:
    if 'mem' in line:
        addr = int(line.split('[',1)[1].split(']')[0])
        val = int(line.split()[-1])

        val |= mask1
        val &= mask0
        mem[addr] = val
    else:
        mask = line.split()[-1]
        
        mask1 = int(mask.replace('X','0'), 2)
        mask0 = int(mask.replace('X','1'), 2)

print(sum(mem.values()))

