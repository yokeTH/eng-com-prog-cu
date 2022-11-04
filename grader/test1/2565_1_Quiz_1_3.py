# 2565_1_Quiz_1_3.py
# Password : quiz_QUIZ

def isNum(s):
    return s in ['0','1','2','3','4','5','6','7','8','9']

s = input()
if s[0] != '-':
    s = '+' + s
    
last = 0
ans = 0

for i in range(0,len(s)):
    if s[i] == '+':
        num = ''
        for j in s[i+1:]:
            if j.isdigit():
                num += j
            else:
                break
        ans += int(num)
    elif s[i] == '-':
        num = ''
        for j in s[i+1:]:
            if j.isdigit():
                num += j
            else:
                break
        ans -= int(num)

print(ans)