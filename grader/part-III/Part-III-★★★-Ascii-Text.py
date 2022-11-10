def lstrip(lns:list):
    lMargin = len(lns[0])
    for ln in lns:
        for i in range(len(ln)):
            if ln[i] != '.' and i < lMargin:
                lMargin = i
                break
    return [ln[lMargin:] for ln in lns]

def rstrip(lns:list):
    rMargin = 0
    for ln in lns:
        for i in range(len(ln)-1)[::-1]:
            if ln[i] != '.' and i > rMargin:
                rMargin = i
                break
    return [ln[:rMargin+1]+'\n' for ln in lns]

def stripAll(lns:list):
    dotIndex = list(range(len(lns[0])))
    for ln in lns:
        for i in range(len(ln)):
            if ln[i] != '.' and i in dotIndex:
                dotIndex.remove(i)
    ans = []
    for ln in lns:
        new = ''
        for i in range(len(ln)):
            if i not in dotIndex:
                new+= ln[i]
        ans.append(new+'')
    return ans
f = open(input()).readlines()
cmd = input()
if cmd == 'LSTRIP':
    print(*lstrip(f),end='',sep='')
elif cmd == 'RSTRIP':
    print(*rstrip(f),end='',sep='')
elif cmd == 'STRIP':
    print(*rstrip(lstrip(f)),end='',sep='')
elif cmd == 'STRIP_ALL':
    print(*stripAll(lstrip(f)),end='',sep='')
else:
    print('Invalid command')