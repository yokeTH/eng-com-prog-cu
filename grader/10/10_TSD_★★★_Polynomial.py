def add_poly(p1, p2):
    ans = []
    for p in p1:
        if len(ans)-1 < p[1]:
            ans += [0]*(p[1]-len(ans)+1)
        ans[p[1]] += p[0]
    for p in p2:
        if len(ans)-1 < p[1]:
            ans += [0]*(p[1]-len(ans)+1)
        ans[p[1]] += p[0]
    return [(y,x) for x,y in enumerate(ans) if y!=0][::-1]

def mult_poly(p1, p2):
    temp = []
    for a in p1:
        for b in p2:
            temp.append((a[0]*b[0],a[1]+b[1]))
    ans = []
    for e in temp:
        ans=add_poly(ans,[e])
    return ans

for i in range(3):
    exec(input().strip())