import string

with open('in/18.in') as fin:
    lines = [x.strip() for x in fin.readlines()]

def apply(a, op, b):
    if op == '+': return a+b
    elif op == '*': return a*b

def solve(line, i = 0):
    val = None
    op = None
    start = i

    while i < len(line):
        if line[i] in string.digits:
            if not val:
                val = int(line[i])
            else:
                val = apply(val, op, int(line[i]))
        
        elif line[i] in "+*":
            op = line[i]
        
        elif line[i] == '(':
            v, c = solve(line, i+1)
            if not val:
                val = v
            else:
                val = apply(val, op, v)
            i += c
        
        elif line[i] == ')':
            i += 1
            break
        
        i += 1
    
    return val, i - start

res = 0
for line in lines:
    res += solve(line)[0]
print(res)
