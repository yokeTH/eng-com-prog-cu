courses = {}
teachers = {}

with open(input()) as f:
    for ln in f:
        num, code = ln.strip().split(',')
        courses[num] = code

with open(input()) as f:
    for ln in f:
        num, name = ln.strip().split(',')
        teachers[num] = name

with open(input()) as f:
    for ln in f:
        col1, col2 = ln.strip().split(',')
        if col1 not in courses or col2 not in teachers:
            print('record error')
        else:
            print('{},{}'.format(courses[col1],teachers[col2]))