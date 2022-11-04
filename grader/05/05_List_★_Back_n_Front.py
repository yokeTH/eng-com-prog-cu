ans = []

def altInsert(l:list, e:any):
    if len(l) % 2 == 0:
        l.append(e)
    else:
        l.insert(0, e)

for _ in range(int(input())):
    altInsert(ans,int(input()))

for i in input().split():
    altInsert(ans,int(i))

while True:
    s = input()
    if s != '-1':
        altInsert(ans,int(s))
    else:
        break

print(ans)