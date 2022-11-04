def day_of_year(d, m, y):
    days = 0
    dayInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

    y-=543

    if y%400 == 0:
        dayInMonth[1]=29
    if y%4 == 0 and y%100 != 0:
        dayInMonth[1]=29

    for i in range(m-1):
        days+= dayInMonth[i]

    return days+d

exec(input())