persons = {}
order = []
for i in range(int(input())):
    ln = input().split(': ')
    persons[ln[0]] = ln[1].split(', ')
    order.append(ln[0])

focus = input()
same = set()
find = False

# print(persons)

for visited in persons[focus]:
    for person in persons:
        if person != focus:
            for city in persons[person]:
                if city[0] == visited[0]:
                    same.add(person)
                    break

if len(same) == 0:
    print('Not Found')
else:
    for e in order:
        if e in same:
            print(e)