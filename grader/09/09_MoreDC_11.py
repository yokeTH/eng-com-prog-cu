lns = [input() for _ in range(int(input()))]

for ln in lns:
    c = 0
    for e in ln:
        if e == '.':
            c+=1
        else:
            break
    print(ln[int(c/2):])