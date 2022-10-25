names = {}
namess = {}
for _ in range(int(input())):
    ln = input().split()
    names[ln[0]] = ln[1]
    namess[ln[1]] = ln[0]

for _ in range(int(input())):
    name = input()
    if name in names:
        print(names[name])
    elif name in namess:
        print(namess[name])
    else:
        print('Not found')