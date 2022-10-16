# 2565_1_Quiz_1_1.py
# Password : quiz_QUIZ

a, b, c, d = [int(e) for e in input().split()]

if a > b:
    a,b = b,a
    while d >= a:
        if c > d:
            a += 1
        else:
            d -= 1
else:
    if c%2 == 0:
        d += a
    else:
        if d > c:
            c += d
        else:
            b += a
        a = b+c
        
print(a,b,c,d)