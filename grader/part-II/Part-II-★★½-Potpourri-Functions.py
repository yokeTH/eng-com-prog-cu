from string import ascii_letters

def convex_polygon_area(p):
    ans = 0
    for i in range(len(p)):
        ans += p[i][0] * p[(i+1)%len(p)][1]
        ans -= p[i][0] * p[(i-1)%len(p)][1]
    return abs(ans / 2)

def is_heterogram(s):
    c = []
    for a in s.split():
        for e in a:
            if e in ascii_letters and e.lower() in c:
                return False
            c.append(e.lower())
    return True

def replace_ignorecase(s, a, b):
    i = s.lower().find(a.lower())
    while i != -1:
        s = s[:i] + b +s[i+len(a):]
        i = s.lower().find(a.lower(),i+len(b))
    return s

def top3(votes):
    temp = []
    for k in votes:
        if votes[k] not in temp:
            temp.append([-votes[k],k])
    temp.sort()
    ans = []
    for k in temp[:3]:
        ans.append(k[1])
    return ans

for k in range(2):
    exec(input().strip())