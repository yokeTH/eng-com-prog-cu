def convert(s):
    nums = 'A23456789TJQK'
    faces = 'CDHS'
    return [nums.find(s[0])+1, faces.find(s[1])+1]

cards = input()
ans = ''
for i in range(0,len(cards)-2,2):
    a = convert(cards[i:i+2])
    b = convert(cards[i+2:i+4])
    if a == b:
        ans += '0'
    elif a[0] == b[0]:
        ans += '+' + str(a[1] - b[1]) if a[1] - b[1]>0 else str(a[1] - b[1])
    else:
        ans += '+' + str(a[0] - b[0]) if a[0] - b[0]>0 else str(a[0] - b[0])

print(ans)