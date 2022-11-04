def upgrade(g):
    if g == 'A':
        return 'A'
    gradeLetters = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
    return gradeLetters[gradeLetters.index(g) - 1]

ids = []
grades = []

s = input()
while s != 'q':
    sid, g = s.split()
    ids.append(sid)
    grades.append(g)
    s = input()

for i in input().split():
    grades[ids.index(i)] = upgrade(grades[ids.index(i)])


for i in sorted(ids):
    print(i, grades[ids.index(i)])
