data = [int(input()) for _ in range(int(input()))]
data.insert(0, data[-1])
data.append(data[1])
pits = []

for i in range(1, len(data) - 1):
    if data[i - 1] > data[i] and data[i + 1] > data[i]:
        pits.append(i - 1)

if len(pits) == 0:
    print("No pits")
else:
    for i in pits:
        print(i)
