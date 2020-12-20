rules = {}
words = []

with open('in/19.in') as fin:
    line = fin.readline().strip()
    while line != '':
        ruleid = int(line.split(':')[0])
        
        line = line.split(':')[1].strip()
        if '"' in line:
            rules[ruleid] = line.split('"')[1]
        else:
            if '|' in line:
                line = [x.strip() for x in line.split('|')]
            else:
                line = [line]

            rules[ruleid] = []
            for item in line:
                rules[ruleid].append(tuple(map(int, item.split())))


        line = fin.readline().strip()
    
    for line in fin:
        words.append(line.strip())

# Add the modified rules
rules[8] = [(42,), (42, 8)]
rules[11] = [(42, 31), (42, 11, 31)]

word_maxlen = max(len(x) for x in words)

literals = {}
for ruleid in rules:
    if type(rules[ruleid]) == str:
        literals[ruleid] = [rules[ruleid][0]]
        
for x in literals:
    del rules[x]

modified = True
while modified:
    modified = False
    
    to_remove = []

    for ruleid in rules:
        rule = rules[ruleid]

        new_rules = []
        for i in range(len(rule)):
            if type(rule[i]) == str: continue
            if type(rule[i]) == list and type(rule[i][0]) == str: continue

            convert = True
            
            for j in range(len(rule[i])):
                if type(rule[i][j]) != str and rule[i][j] not in literals:
                    convert = False
            
            if convert:
                print(f'Converting clause {ruleid}:{i}')
                modified = True
                res = ['']
                for term in rule[i]:
                    #print(term)
                    
                    new_terms = []
                    for j in range(len(res)):
                        for x in literals[term][1:]:
                            if len(res[j]+x) <= word_maxlen:
                                new_terms.append( res[j] + x )
                        res[j] += literals[term][0]
                    res += new_terms
                
                if len(res) < 32:
                    print('  ->', res)
                else:
                    print('  ->', len(res), 'terms')
                
                rule[i] = res[0]
                for x in res[1:]:
                    new_rules.append(x)
        rules[ruleid] += new_rules
        
        #print(rule)
        if all(type(x) == str for x in rule):
            print('Literalizing rule', ruleid)
            modified = True

            to_remove.append(ruleid)
            literals[ruleid] = list(set(rule))
            #print(literals)


    for x in to_remove:
        del rules[x]



    if len(rules) == 0: break
    print(len(rules))

#print(rules)
#print(literals[31])

# 42* 8 42^n 11 31^n  <- pattern
# 8m  8 8n   16 8n    <- length of each token

elems8 =  set(x for x in rules[8] if type(x) == str)
elems11 = set(x for x in rules[11] if type(x) == str)
elems31 = set(literals[31])
# The literals in 42, 31 and 11 are all disjoint
assert len(set(literals[42]).intersection(set(literals[31]))) == 0
# The literals in 42 and 8 are the same
assert set(literals[42]) == elems8

def check(word):
    for n in range(6):

        if (2*n+3)*8 > len(word): continue

        pieces = []
        for i in range(0, len(word), 8):
            pieces.append(word[i:i+8])
        
        fail = False
        for i in range(len(word)//8-2-n):
            if pieces[0] not in elems8:
                fail = True
                break
            pieces = pieces[1:]

        if fail:
            continue

        if pieces[0]+pieces[1] not in elems11:
            continue
        pieces = pieces[2:]

        for x in pieces:
            if x not in elems31:
                fail = True
                break
        
        if not fail:
            return True
    return False

ctr = 0
for x in words:
    if check(x):
        ctr += 1
print(ctr)
