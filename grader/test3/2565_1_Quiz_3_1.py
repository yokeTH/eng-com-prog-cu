# 2565_1_Quiz_3_1.py

teams = {}

for i in range(int(input())):
    teamName, country = input().split()
    teams[teamName] = country

ln = input()
ans = []
while ln != 'q':
    valid = True
    temp = []
    for i in ln.split():
        if i not in teams or teams[i] in temp:
            valid = False
        else:
            temp.append(teams[i])
    if valid:
        ans.append('OK')
    else:
        ans.append('Not OK')
    ln = input()

print(*ans,sep='\n')