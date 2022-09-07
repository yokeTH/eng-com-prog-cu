data = []

num = input()
while num != 'q':
    data.append(float(num))
    num = input()

if len(data) != 0:
    print(round(sum(data)/len(data),2))
else:
    print('No Data')