def str2RLE(t):
    chars = []
    cnts = []

    while len(t):
        chars.append(t[0])
        privLen = len(t)
        t = t.lstrip(t[0])
        cnts.append(privLen-len(t))

    ans = ''
    for i in range(len(chars)):
        ans += chars[i] + ' ' + str(cnts[i]) + ' '

    print(ans.strip())

def RLE2str(t):
    ans = ''
    p = t.split()
    for i in range(0, len(p), 2):
        ans += p[i] * int(p[i+1])
    print(ans)

cmd = input()
if cmd == 'str2RLE':
    str2RLE(input())
elif cmd == 'RLE2str':
    RLE2str(input())
else:
    print('Error')