def peaks(x):
    pos = []

    for i in range(len(x)):
        if i != 0 and i != len(x) - 1:
            priv = x[i-1]
            now = x[i]
            next_ = x[i+1]
            if priv < now and next_ < now:
                pos.append(i)

    return pos

exec(input())
