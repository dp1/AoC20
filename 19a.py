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

word_maxlen = max(len(x) for x in words)

literals = {}
for ruleid in rules:
    if type(rules[ruleid]) == str:
        literals[ruleid] = [rules[ruleid][0]]
        
for x in literals:
    del rules[x]

while True:
    
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

            to_remove.append(ruleid)
            literals[ruleid] = list(set(rule))
            #print(literals)


    for x in to_remove:
        del rules[x]



    if len(rules) == 0: break
    print(len(rules))
    #input()


ctr = 0
target = set(literals[0])
for x in words:
    if x in target:
        ctr += 1
print(ctr)
