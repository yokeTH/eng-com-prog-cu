filename, year = input().split()
scores = []
with open(filename) as f:
    ln = f.readline()
    while ln:
        sid, score = ln.strip().split()
        if sid[:2] == year[-2:]:
            scores.append(float(score))
        ln = f.readline()
if scores != []:
    print(min(scores), max(scores), sum(scores)/len(scores))
else:
    print('No data')