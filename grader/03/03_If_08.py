dayInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
d = int(input())
m = int(input())
y = int(input())

y-=543

if y%400 == 0:
    dayInMonth[1]=29
if y%4 == 0 and y%100 != 0:
    dayInMonth[1]=29

days = 0
for i in range(m-1):
    days+= dayInMonth[i]

days+=d
print(days)