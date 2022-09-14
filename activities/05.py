y = input() + '$'
rotated = []
for i in range(len(y)):
    rotated.append(y[i:]+y[:i])
rotated.sort()
ans = ''
for i in rotated:
    ans+=i[-1]
print(ans)