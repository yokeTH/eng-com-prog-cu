def missing_digits(t):
    nums = ['0','1','2','3','4','5','6','7','8','9']

    for i in t:
        if i in nums:
            nums.remove(i)

    return [int(i) for i in nums]

exec(input())