animals = {}
keys = []

ln = input()
while ln.lower() != 'q':
    name, typeof = ln.split(', ')
    if typeof in animals:
        animals[typeof].append(name)
    else:
        animals[typeof] = [name]
        keys.append(typeof)
    ln = input()
    

for k in keys:
    print('{}: {}'.format(k,', '.join(animals[k])))