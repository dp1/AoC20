import string

with open('in/18.in') as fin:
    lines = [x.strip() for x in fin.readlines()]

def to_rpn(line):
    ops = []
    out = ''
    for ch in line:
        if ch in string.digits:
            out += ch
        
        elif ch == '+':
            while len(ops) > 0 and ops[-1] == '+':
                out += ops[-1]
                ops.pop()

            ops.append(ch)
        
        elif ch == '*':
            while len(ops) > 0 and ops[-1] == '+':
                out += ops[-1]
                ops.pop()
            ops.append(ch)
        
        elif ch == '(':
            ops.append(ch)
        
        elif ch == ')':
            while len(ops) > 0 and ops[-1] != '(':
                out += ops[-1]
                ops.pop()
            if len(ops) > 0: ops.pop() # Remove '('
        
    while len(ops) > 0:
        out += ops[-1]
        ops.pop()
    
    return out

def apply(a, op, b):
    if op == '+': return a+b
    elif op == '*': return a*b

def solve(line):
    line = to_rpn(line)
    s = []

    for ch in line:
        if ch in string.digits:
            s.append(int(ch))
        
        else:
            a, b = s[-1], s[-2]
            s.pop(); s.pop()
            s.append(apply(a, ch, b))
    
    return s[-1]

res = 0
for line in lines:
    res += solve(line)
print(res)
