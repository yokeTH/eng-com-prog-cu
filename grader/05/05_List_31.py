import math


def c(l):
    return l[math.ceil(len(l)/2):] + l[:math.floor(len(l)/2)]

def s(l):
    ans = []
    for i in range(int(len(l)/2)):
        ans.append(l[i])
        ans.append(l[int(len(l)/2)+i])
    return ans

deck = input().split()

for i in input():
    if i == 'C':
        deck = c(deck)
    elif i == 'S':
        deck = s(deck)

print(*deck)