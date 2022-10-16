import math


par = 0
stroke = 0
update = 0

for _ in range(9):
    a, b, c = [int(e) for e in input().split()]
    par += a
    stroke += b
    if c == 1:
        update += min(a+2,b)

tamTor = math.floor(0.8*((1.5*update)-par))

print(stroke)
print(tamTor)
print(stroke - tamTor)