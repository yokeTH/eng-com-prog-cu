def index_of(grades, ID):
    for i in range(len(grades)):
        if grades[i][0] == ID:
            return i
    return -1

def up(g):
    if g == 'A':
        return 'A'
    gradeLetters = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
    return gradeLetters[gradeLetters.index(g) - 1]

def upgrade(grades, IDs):
    for i in IDs:
        index = index_of(grades,i)
        if index != -1:
            grades[index][1] = up(grades[index][1])

    grades.sort()



exec(input())
exec(input())
exec(input())