s = ''
i = 0

while s != 'Zag-Zig' and s != 'Zig-Zag':
    s = input()
    exec('n{} = [int(j) for j in s.split()]'.format(i))

x = 0 if s == 'Zag-Zig' else 1

for j in range(0+1+x,i+1+x):
    if j == 0+x:
        mini, maxi = n1[i%2], n1[(i+1) %2]

    if mini > exec('n{}[i%2]'.format(j)):
        mini = exec('n{}[i%2]'.format(j))
    if maxi < exec('n{}[(i+1)%2]'.format(j)):
        maxi = exec('n{}[(i+1)%2]'.format(j))

print(mini, maxi)