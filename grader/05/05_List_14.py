y = [float(i) for i in input().split()]

cnt = 0

for i in range(len(y)):
    if i != 0 and i != len(y) - 1:
        priv = y[i-1]
        now = y[i]
        next_ = y[i+1]
        if priv < now and next_ < now:
            cnt+=1

print(cnt)