def make_int_list(x):
    return [int(e) for e in x.split()]

def is_odd(e):
    return e % 2 == 1

def odd_list(alist):
    ans = []
    for e in alist:
        if is_odd(e):
            ans.append(e)
    return ans

def sum_square(alist):
    return sum([e**2 for e in alist])

exec(input().strip())