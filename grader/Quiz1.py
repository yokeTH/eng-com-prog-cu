x = [int(e) for e in input().split()]
k = int(input())

num = [x[0]]
c = [0]

for e in x:
    if num[-1] == e:
        c[-1] += 1
    else:
        num.append(e)
        c.append(1)

ans = 0

for i in range(len(c)):
    if c[i] < k:
        ans += c[i] * num[i]

print(ans)