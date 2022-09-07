p = float(input())
k, t = 1, 1

t *= (366-k) / 365

while not 1-t >= p:
    k+=1
    t *= (366-k) / 365


print(k)