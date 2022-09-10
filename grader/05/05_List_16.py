n = int(input())
seq = [n]

while n != 1:
    if n%2 == 0:
        n = int(n/2)
    else:
        n = 3*n + 1
    seq.append(n)

print(*seq[-15:], sep='->')