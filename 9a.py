with open('in/9.in', 'r') as fin:
    data = [int(x) for x in fin.readlines()]

preamble, data = data[:25], data[25:]

# O(25^2*N) -> O(N)

for x in data:
    
    for y in preamble:
        if x-y in preamble: break
    else:
        print(x)
    
    preamble = preamble[1:] + [x]
