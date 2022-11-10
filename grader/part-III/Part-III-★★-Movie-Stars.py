movies = {}

for _ in range(int(input())):
    name, actor1, actor2 = input().split(', ')
    if actor1 in movies:
        movies[actor1].append(name)
    else:
        movies[actor1] = [name]

    if actor2 in movies:
        movies[actor2].append(name)
    else:
        movies[actor2] = [name]

for name in input().split(', '):
    if name in movies:
        print('{} -> {}'.format(name, ', '.join(movies[name])))
    else:
        print('{} -> Not found'.format(name))