coord = []

for i in range(int(input())):
    coord.append([float(i) for i in input().split()] + [i+1])

distance = []

for i in coord:
    distance.append(i[0]**2 + i[1]**2)

print('#{0[2]}: ({0[0]}, {0[1]})'.format(coord[distance.index(sorted(distance)[2])]))
