with open('1.in', 'r') as fin:
    nums = list(map(int, fin.readlines()))

s = set(nums)
for x in nums:
    if x <= 2020-x and 2020 - x in s:
        print((2020-x)*x)
