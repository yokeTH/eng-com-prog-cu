members = {}
otas = {}
ln = input()
while len(ln) > 1:
    ota, name, score = ln.split()
    if name in members:
        members[name]['otas'].add(ota)
        members[name]['score'] += int(score)
    else:
        members[name] = {'otas':{ota},'score':int(score),'kami':set()}
    if ota in otas:
        if otas[ota]['kami'] == name:
            otas[ota]['score'] += int(score)
        elif otas[ota]['score'] == int(score) and otas[ota]['kami'] > name:
            otas[ota]['kami'] = name
        elif otas[ota]['score'] < int(score):
            otas[ota]['score'] = int(score)
            otas[ota]['kami'] = name
    else:
        otas[ota] = {'score': int(score), 'kami': name}
    ln = input()

for k in otas:
    members[otas[k]['kami']]['kami'].add(k)

rawAns = []

if ln == '1':
    for k in members:
        rawAns.append([-members[k]['score'],k])
elif ln == '2':
    for k in members:
        rawAns.append([-len(members[k]['otas']),k])
elif ln == '3':
    for k in members:
        rawAns.append([-len(members[k]['kami']),k])

rawAns.sort()
ans = []
for e in rawAns[:3]:
    ans.append(e[1])
print(*ans,sep=', ')