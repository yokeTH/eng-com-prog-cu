nums = ['0','1','2','3','4','5','6','7','8','9']

for i in input():
    if i in nums:
        nums.remove(i)

if len(nums) == 0:
    print(None)
else:
    print(*nums, sep=',')