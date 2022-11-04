names = {}
names2 = {}
for _ in range(int(input())):
    ln = input().split()
    names[ln[0]+' '+ln[1]] = ln[2]
    names2[ln[2]] = ln[0]+' '+ln[1]

final = []

for _ in range(int(input())):
    final.append(input())

for name in final:
    if name in names:
        print(name,'-->',names[name])
    elif name in names2:
        print(name,'-->',names2[name])
    else:
        print(name,'-->','Not found')