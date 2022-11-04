from calendar import month_name

d, m, y = input().split('/')

print("{} {}, {}".format(month_name[int(m)], d, y))
