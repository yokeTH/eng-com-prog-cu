partysSeq = []
partys = {}
members = {}

for _ in range(int(input())):
    partyName = input()
    partysSeq.append(partyName)
    partys[partyName] = {'score':{'Y':0, 'N':0, 'X':0}, 'members':[]}

for _ in range(int(input())):
    name, party = input().split()
    members[name] = {'party':party, 'voted': False}
    partys[party]['members'].append(name)

for _ in range(int(input())):
    name, vote = input().split()
    partys[members[name]['party']]['score'][vote] += 1
    members[name]['voted'] = True
    members[name]['vote'] = vote

for partyName in partysSeq:
    countMax = 0
    countZero = 0
    conclu = ''

    for k in partys[partyName]['score']:
        if partys[partyName]['score'][k] == max(partys[partyName]['score'].values()):
            countMax += 1
            conclu = k
        if partys[partyName]['score'][k] == 0:
            countZero += 1

    print(partyName)
    if countZero > 1:
        print('No cobra')
    elif countMax > 1:
        print('Inconclusive')
    else:
        cobra = []
        for member in partys[partyName]['members']:
            if members[member]['voted'] and members[member]['vote'] != conclu:
                cobra.append(member)
        print(', '.join(sorted(cobra)))