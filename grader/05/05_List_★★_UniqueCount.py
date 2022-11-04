data = []
for i in sorted([int(i) for i in input().split()]):
    if len(data) != 0:
        if int(i) > data[-1]:
            data.append(int(i))
    else:
        data.append(int(i))

cnt = 1

for i in range(len(data)):
    if i != 0:
        if data[i-1] < data[i]:
            cnt+=1

print(cnt)
print(data[:10])