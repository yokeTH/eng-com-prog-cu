def RLE(t):
    chars = []
    cnts = []

    while len(t):
        chars.append(t[0])
        privLen = len(t)
        t = t.lstrip(t[0])
        cnts.append(privLen-len(t))

    ans = []
    for i in range(len(chars)):
        ans.append([chars[i],cnts[i]])

    return ans

exec(input())