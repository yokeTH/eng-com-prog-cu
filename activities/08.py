songs = {}

ln = input()
while ln.lower() != 'q':
    s = ln.split(',')
    if s[-1].strip() not in songs:
        songs[s[-1].strip()] = []
    for i in range(len(s) - 1):
        songs[s[-1].strip()].append(s[i].strip())
    ln = input()

for k in songs:
    print(k+':', ', '.join(songs[k]))