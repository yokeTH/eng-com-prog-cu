iceCreams = {}
for _ in range(int(input())):
    name, price = input().split()
    iceCreams[name] = float(price)

orders = {}
for _ in range(int(input())):
    name, amont = input.split()
    if name in iceCreams:
        if name not in orders:
            orders[name] = 0
        orders[name] += int(amont)

top = []
total = 0
for name in orders:
    top.append([-1*iceCreams[name]*orders[name], name])
    total += iceCreams[name]*orders[name]
top.sort()

if len(top) == 0:
    print('No ice cream sales')
else:
    print('Total ice cream sales: '+str(float(total)))
    ans = []
    for ice in top[:3]:
        ans.append(ice[1])
    print('Top sales : '+ ', '.join(ans))