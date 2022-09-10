m = int(input())
p1 = 0
p2 = 0
cnt = 0

while p1 < m and p2 < m and 3*m < cnt:
    a, b = input().split()

    if a == 'R':
        if b == 'P':
            p2+=1
        elif b == 'S':
            p1+=1
    elif a == 'S':
        if b == 'P':
            p1+=1
        elif b == 'R':
            p2+=1
    else:
        if b == 'R':
            p1+=1
        elif b == 'S':
            p2+=1

print(p1, p2)
print