u,i = set(),set()

for k in range(int(input())):
    s = {int(i) for i in input().split()}
    if k == 0:
        u,i = s,s
    else:
        u= u | s
        i= i & s

print(len(u))
print(len(i))