bidders = {}
products = {}

cnt = 0
total = int(input())

while cnt < total:
    ln = input().split()
    if ln[0] == 'B':
        if ln[1] not in bidders:
            bidders[ln[1]] = {'got':[], 'toPay':0}
        bidders[ln[1]][ln[2]] = int(ln[3])

        if ln[2] not in products:
            products[ln[2]] = {'top':0, 'win':None ,'bit':{}}
        products[ln[2]]['bit'][ln[1]] = int(ln[3])

        if int(ln[3]) > products[ln[2]]['top']:
            products[ln[2]]['top'] = int(ln[3])
            products[ln[2]]['win'] = ln[1]
    elif ln[0] == 'W':
        if ln[2] in bidders[ln[1]]:
            del bidders[ln[1]][ln[2]]
        if ln[1] in products[ln[2]]['bit']:
            del products[ln[2]]['bit'][ln[1]]

        if ln[1] == products[ln[2]]['win']:
            products[ln[2]]['win'] = None
            products[ln[2]]['top'] = 0
            for k in products[ln[2]]['bit']:
                if products[ln[2]]['bit'][k] > products[ln[2]]['top']:
                    products[ln[2]]['win'] = k
                    products[ln[2]]['top'] = products[ln[2]]['bit'][k]
    else:
        cnt -= 1
        print('Not B W')
    cnt += 1


for i in products:
    if products[i]['win'] != None:
        bidders[products[i]['win']]['got'].append(i)

for i in bidders:
    for j in bidders[i]['got']:
        bidders[i]['toPay']+= products[j]['top']

for i in sorted(bidders):
    if bidders[i]['got'] != []:
        print('{}: ${} -> {}'.format(i,bidders[i]['toPay'],' '.join(sorted(bidders[i]['got']))))
    else:
        print('{}: $0'.format(i))