from string import ascii_letters
ans = {}
s = input()
for e in s:
    if e in ascii_letters:
        if e.lower() in ans:
            ans[e.lower()] += 1
        else:
            ans[e.lower()] = 1

temp = []
for k in ans:
    temp.append([-ans[k],k])

for e in sorted(temp):
    print(e[1],'->',-e[0])