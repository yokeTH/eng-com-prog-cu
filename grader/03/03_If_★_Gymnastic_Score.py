data = [float(i) for i in input().split()]

min = data[0]
max = data[0]
for i in data:
    if i > max:
        max = i
    if i < min:
        min = i

data.remove(min)
data.remove(max)

print(round(sum(data)/len(data),2))