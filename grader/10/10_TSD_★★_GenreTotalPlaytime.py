catergories = {}
for _ in range(int(input())):
    ln = input().split(', ')
    time = ln[-1].split(':')
    if ln[-2] in catergories:
        catergories[ln[-2]] += int(time[0])*60 + int(time[1])
    else:
        catergories[ln[-2]] = int(time[0])*60 + int(time[1])

sort = sorted([[-catergories[k],k] for k in catergories])

for e in sort[:3]:
    print('{} --> {}:{:02d}'.format(e[1], (-e[0])//60, (-e[0])%60))