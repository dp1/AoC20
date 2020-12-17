ranges = {}

with open('in/16.in') as fin:

    line = fin.readline().strip()
    while line != '':
        a, b = line.split()[-3::2]
        a = list(map(int, a.split('-')))
        a = range(a[0], a[1]+1)
        b = list(map(int, b.split('-')))
        b = range(b[0], b[1]+1)
        name = line.split(':')[0]
        ranges[name] = (a,b)
        line = fin.readline().strip()
    
    fin.readline()
    my_ticket = list(map(int, fin.readline().split(',')))
    fin.readline()
    fin.readline()

    tickets = []
    for line in fin:
        ticket = list(map(int, line.strip().split(',')))
        valid = True
        for x in ticket:
            for r in ranges:
                if x in ranges[r][0] or x in ranges[r][1]:
                    break
            else:
                valid = False
        
        if valid:
            tickets.append(ticket)


    matching = {}
    matched_idx = set()

    # Find one element at a time
    for _ in range(len(my_ticket)):

        # Get candidate indices for each umatched item
        candidates = {}
        for item in ranges:
            if item in matching: continue
            candidates[item] = []

            for i in range(len(my_ticket)):
                if i in matched_idx: continue

                for ticket in tickets:
                    if ticket[i] not in ranges[item][0] and ticket[i] not in ranges[item][1]:
                        break
                else:
                    candidates[item].append(i)
        
        for item in ranges:
            if item not in matching and len(candidates[item]) == 1:
                i = candidates[item][0]
                matched_idx.add(i)
                matching[item] = i
                print(f'{item} -> column {i}')
                break
        else:
            print('No match :(')
            exit(1)
    
    res = 1
    for item in ranges:
        if item.startswith('departure'):
            res *= my_ticket[matching[item]]
    print(res)
