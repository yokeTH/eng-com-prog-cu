

n1 = [int(i) for i in input().split()]
n2 = [int(i) for i in input().split()]
n3 = [int(i) for i in input().split()]

x = 0 if input() == 'Zag-Zig' else 1

i = 0 + x
mini, maxi = n1[i%2], n1[(i+1) %2]
i+= 1

if mini > n1[i%2]:
    mini = n1[i%2]
if maxi < n1[(i+1) %2]:
    maxi = n1[(i+1) %2]
i+=1

if mini > n2[i%2]:
    mini = n2[i%2]
if maxi < n2[(i+1) %2]:
    maxi = n2[(i+1) %2]
i+=1

if mini > n3[i%2]:
    mini = n3[i%2]
if maxi < n3[(i+1) %2]:
    maxi = n3[(i+1) %2]

print(mini, maxi)