with open('in/10.in', 'r') as fin:
    data = sorted([int(x) for x in fin.readlines()])

data = [0] + data
ctr = [0 for _ in range(len(data))]
ctr[0] = 1

for i in range(len(data)):
    for j in range(i+1,i+4):
        if j < len(data) and data[j] <= data[i] + 3:
            ctr[j] += ctr[i]

print(ctr[-1])
