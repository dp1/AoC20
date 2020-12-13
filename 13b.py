from sympy.ntheory.modular import crt

with open('in/13.in') as fin:
    fin.readline()
    V = fin.readline().strip().split(',')

m, v = [], []
for i,x in enumerate(V):
    if x != 'x':
        m.append(int(x))
        v.append(i)

res = crt(m, v)
print(res[1] - res[0])
