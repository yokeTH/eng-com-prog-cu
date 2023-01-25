movies = {}
for _ in range(int(input())):
    title, actor1, actor2 = input().split(', ')
    if actor1 not in movies:
        movies[actor1] = []
    movies[actor1].append(title)

    if actor2 not in movies:
        movies[actor2] = []
    movies[actor1].append(title)

for actor in input().split(', '):
    if actor in movies:
        print(actor+' -> '+', '.join(movies[actor]))
    else:
        print(actor+' -> Not found')