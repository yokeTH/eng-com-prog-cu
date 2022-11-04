data = input()

temp = '%03d' % (
    (int(data[3] + data[10] + data[17] + data[24] + data[31]) +
     int(data[7] + data[12] + data[17] + data[22] + data[27]) + 10000) %
    10000 // 10)

print(temp + chr(sum([int(i) for i in temp]) % 10 + 65))
