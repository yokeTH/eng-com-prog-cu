def RLE(t):
    ans = []
    cnt = 1
    for i in range(len(t)):
        if i != 0:
            if t[i] != t[i-1]:
                ans.append([t[i-1], cnt])
                cnt = 1
            else:
                cnt+=1
        if i == len(t) - 1:
            ans.append([t[-1], cnt])
    return ans

exec(input())