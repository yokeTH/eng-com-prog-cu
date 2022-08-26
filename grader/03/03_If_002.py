d, m, y = [int(i) for i in input().split()]

y-=543
n=31

thirtyDayMonth = [4,6,9,11]

if m in thirtyDayMonth:
    n=30
elif m == 2:
    n=28
    if y%400 == 0:
        n=29
    if y%4 == 0 and y%100 != 0:
        n=29

d+=15

if d>n:
    d-=n
    m+=1

if m>12:
    m-=12
    y+=1

y+=543

print('{}/{}/{}'.format(d,m,y))