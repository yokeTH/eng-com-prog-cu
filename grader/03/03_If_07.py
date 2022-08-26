suffix = ''

views = int(input())

if views > 10**9:
    suffix = 'B'
    views/=10**9
elif views > 10**6:
    suffix = 'M'
    views/=10**6
elif views > 10**3:
    suffix = 'K'
    views/=10**3

if views > 10:
    views = int(round(views,0))
else:
    views = round(views,1)

print(str(views)+suffix)