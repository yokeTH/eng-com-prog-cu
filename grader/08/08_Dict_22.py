ices={}

for _ in range(int(input())):
    ln = input().split()
    ices[ln[0]] = int(ln[1])

ordersList = []
for _ in range(int(input())):
    ln = input().split()
    if ln[0] in ices:
        ordersList.append([int(ln[1])*ices[ln[0]], ln[0]])

ordersDict = {}
for e in ordersList:
    if e[1] in ordersDict:
        ordersDict[e[1]] += e[0]
    else:
        ordersDict[e[1]] = e[0]

ordersList = []
for k in ordersDict:
    ordersList.append([-ordersDict[k], k])
ordersList.sort()

if len(ordersList) == 0:
    print('No ice cream sales')
else:
    total = 0
    for e in ordersList:
        total += -e[0]
    print('Total ice cream sales: {:.1f}'.format(total))
    topSaleStr = ordersList[0][1]
    for e in range(1,len(ordersList)):
        if ordersList[e][0] != ordersList[0][0]:
            break
        else:
            topSaleStr += ', '+ordersList[e][1]
    print('Top sales:', topSaleStr)