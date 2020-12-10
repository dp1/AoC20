with open('in/1.in', 'r') as fin:
    nums = list(map(int, fin.readlines()))

m = {}
for x in nums:
    if x not in m: m[x] = 0
    m[x] += 1

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        x = 2020 - nums[i] - nums[j]
        ctr = 1
        if x == i: ctr += 1
        if x == j: ctr += 1

        if x in m and m[x] >= ctr:
            print(nums[i] * nums[j] * x)
