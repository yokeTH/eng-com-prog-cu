# 2565_1_Quiz_3_2.py

n, m, k = [int(i) for i in input().split()]

bundits = {}
guests = {}

for i in range(n):
    name, fac = input().split()
    bundits[name] = fac

for i in range(m):
    ln = input().split()
    name = ln[0]
    fac = set(bundits[name] for name in ln[1:])
    guests[name] = fac

for i in range(k):
    g = input().split()
    s = guests[g[0]]
    for name in g:
        s &= guests[name]
    if len(s) == 0:
        print(None)
    else:
        print(*sorted(list(s)),sep=' ')