persons = {}
order = []
for i in range(int(input())):
    ln = input().split(': ')
    persons[ln[0]] = ln[1].split(', ')
    order.append(ln[0])

focus = input()
same = {}
find = False

for visited in persons[focus]:
    for person in persons:
        for city in persons[person]:
            if visited[0] == city[0]:
                print(person)
                break
