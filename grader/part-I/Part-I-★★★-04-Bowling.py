scores = []
ln = input()

def findNext(i, ln):
    for j in range(i+1,len(ln)):
        if ln[j] != 'X' and ln[j] != '/':
            return int(ln[j]),j
    return 10, None

for i in range(len(ln)):
    if ln[i] == 'X':
        frameScore = 0
        score, j = findNext(i, ln)
        frameScore+= score
        score, j = findNext(j, ln)
        frameScore+= score
        scores.append(frameScore)
    elif ln[i] == '/':
        frameScore = 0
        score, j = findNext(i, ln)
        frameScore+= score
    else: