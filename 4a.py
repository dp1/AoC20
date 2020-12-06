with open('4.in', 'r') as fin:
    lines = fin.readlines()

passports = []
cur = {}
for line in lines + ['']:
    if len(line.strip()) == 0:
        passports.append(cur)
        cur = {}
    else:
        for field in line.strip().split():
            k,v = field.split(':')
            cur[k] = v

mandatory = ['byr','iyr','eyr','hgt','hcl','ecl','pid']#,'cid']

ctr = 0
for passport in passports:
    for k in mandatory:
        if k not in passport:
            break
    else:
        ctr += 1

print(ctr)
