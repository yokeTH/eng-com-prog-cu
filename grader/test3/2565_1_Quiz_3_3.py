# 2565_1_Quiz_3_3.py

allys = {}
enemys = {}
tables = []

def isEnemy(c1, c2):
    yes = False
    if c1 not in allys:
        ally1 = {c1}
    else:
        ally1 = allys[c1]

    if c2 not in allys:
        ally2 = {c2}
    else:
        ally2 = allys[c2]

    for i in ally1:
        for j in ally2:
            if i in enemys and enemys[i] == j:
                yes = True
                break
            elif j in enemys and enemys[j] == i:
                yes = True
                break
        if yes:
            break
    return yes


ln = input()
while ln != 'End':
    splited = ln.split()
    mode = splited[0]
    countries = splited[1:]
    if mode == 'Ally':
        for country in countries:
            allys[country] = set(countries)
            
    elif mode == 'Enemy':
        for country in countries:
            country1,country2 = countries
            enemys[country1] = country2
            enemys[country2] = country1
    
    elif mode == 'Table':
        valid = True  
        for i in range(len(countries)):
            if isEnemy(countries[i],countries[(i+1)%len(countries)]):
                valid = False 
                break
        if valid:
            print('Okay')
        else:
            print('No')
    ln = input()