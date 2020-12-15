with open('in/14.in') as fin:
    lines = [x.strip() for x in fin.readlines()]

mem = {}
mask1, maskX = 0, 0
X = []

for line in lines:
    if 'mem' in line:
        addr = int(line.split('[',1)[1].split(']')[0])
        val = int(line.split()[-1])

        addr |= mask1
        addr &= maskX

        for v in X:
            mem[addr + v] = val
    else:
        mask = line.split()[-1]
        #print(mask.count('X')) # luckily, no more than 9
        
        mask1 = int(mask.replace('X','0'), 2)
        maskX = int(mask.replace('0','1').replace('X','0'), 2)
        Xi = []
        for i in range(36):
            if maskX & (2**i) == 0:
                Xi.append(i)
        X = []
        for i in range(2**len(Xi)):
            v = 0
            for j in range(len(Xi)):
                if i & (2**j) != 0:
                    v += 2**Xi[j]
            X.append(v)

print(sum(mem.values()))
