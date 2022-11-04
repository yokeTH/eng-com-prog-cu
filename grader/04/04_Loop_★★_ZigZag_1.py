zig = []
zag = []

for i in range(int(input())):
    x,y = [int(i) for i in input().split()]
    if i%2 == 1:
        zig.append(x)
        zag.append(y)
    else:
        zig.append(y)
        zag.append(x)

if input() != 'Zag-Zig':
    zig,zag = zag,zig

print(min(zig), max(zag))