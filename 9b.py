with open('9.in', 'r') as fin:
    data = [int(x) for x in fin.readlines()]

preamble, elems = data[:25], data[25:]

# O(25^2*N) -> O(N)

target = None
for x in elems:
    
    for y in preamble:
        if x-y in preamble: break
    else:
        target = x
        break
    
    preamble = preamble[1:] + [x]

assert target is not None

# Two pointers, O(N)

right = 0
current = 0
for left in range(len(data)):
    
    if left > 0:
        current -= data[left-1]
    
    while right < len(data) and current < target:
        current += data[right]
        right += 1
    
    if current == target and left < right - 1:
        a = min(data[left:right])
        b = max(data[left:right])
        print(a+b)
