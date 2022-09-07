fname = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nickname = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

people = []

for _ in range(int(input())):
    people.append(input())

for i in people:
    if i in fname:
        print(nickname[fname.index(i)])
    elif i in nickname:
        print(fname[nickname.index(i)])
    else:
        print('Not found')