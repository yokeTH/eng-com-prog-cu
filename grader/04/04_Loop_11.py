s = input()
privLen = len(s)

while len(s):
    print(s[0], end=' ')
    privLen = len(s)
    s = s.lstrip(s[0])
    print(privLen - len(s), end=' ')