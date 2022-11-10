stu = {}

for _ in range(int(input())):
    ln = input().split()
    stu[ln[0]] = ln[1:]

s = input().split()

search = []

for i in s[0]:
    for st in stu:
        for e in stu[st]:
            if i == e:
                search.append(st)

for st in search:

print('='*30)

cnt = {}
for e in search:
    if e in cnt:
        cnt[e]+=1
    else:
        cnt[e]=1


if len(cnt)!=[]:
    most = max(cnt.values())
    ans = []
    for k in cnt:
        if cnt[k] == most:
            ans.append(k)
    for e in sorted(ans):
        print(e,*stu[e],sep=' ')
else:
    print('Not Found')