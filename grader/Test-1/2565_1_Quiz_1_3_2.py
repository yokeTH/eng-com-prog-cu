# 2565_1_Quiz_1_3.py
# Password : quiz_QUIZ

s = input()
if s[0] != '-':
    s = '+' + s

ans = 0
op = []

for i in range(0,len(s)):
    if s[i] == '+' or s[i] == '-':
        op.append(i)
        
for i in range(len(op)-1):
    if s[op[i]] == '+':
        ans += int(s[op[i]+1:op[i+1]])
    if s[op[i]] == '-':
        ans -= int(s[op[i]+1:op[i+1]])
        
if s[op[-1]] == '+':
        ans += int(s[op[-1]+1:])
if s[op[-1]] == '-':
        ans -= int(s[op[-1]+1:])

print(ans)
