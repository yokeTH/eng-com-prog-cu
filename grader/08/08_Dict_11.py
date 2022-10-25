def reverse(d):
    ans = {}
    for k in d:
        ans[d[k]] = k
    return ans

def keys(d, v):
    ans = []
    for k in d:
        if v == d[k]:
            ans.append(k)
    return ans

exec(input().strip())