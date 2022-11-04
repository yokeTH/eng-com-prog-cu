from string import ascii_letters
s = []
anagram = []

for i in input():
    if i in ascii_letters:
        s.append(i.lower())

for i in input():
    if i in ascii_letters:
        anagram.append(i.lower())

s.sort()
anagram.sort()

if s == anagram:
    print('YES')
else:
    print('NO')