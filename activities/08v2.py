songs = {'Pop':[],'R&B':[],'Rock':[]}

ln = input()
while ln.lower() != 'q':
    s = ln.split(', ')
    for i in range(len(s) - 1):
        songs[s[-1]].append(s[i].strip())
    ln = input()

for k in songs:
    print(k+':', ', '.join(songs[k]))