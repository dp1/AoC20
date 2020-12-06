import string

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
for p in passports:
    for k in mandatory:
        try:
            if k not in p: break
            if k == 'byr' and int(p['byr']) not in range(1920, 2003): break
            if k == 'iyr' and int(p['iyr']) not in range(2010, 2021): break
            if k == 'eyr' and int(p['eyr']) not in range(2020, 2031): break

            if k == 'hgt' and p['hgt'][-2:] == 'cm':
                if int(p['hgt'][:-2]) not in range(150, 194): break
            elif k == 'hgt' and p['hgt'][-2:] == 'in':
                if int(p['hgt'][:-2]) not in range(59, 77): break
            elif k == 'hgt': break
            
            if k == 'hcl':
                if p['hcl'][0] != '#' or len(p['hcl']) != 7 or any([x not in '0123456789abcdef' for x in p['hcl'][1:]]): break
            if k == 'ecl' and p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: break
            if k == 'pid' and (len(p['pid']) != 9 or any([x not in string.digits for x in p['pid']])): break
        except ValueError:
            break
    else:
        ctr += 1

print(ctr)
