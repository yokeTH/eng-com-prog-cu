grade = {'A':4, 'B':3, 'C':2, 'D':1}

student1 = input().split()
student2 = input().split()

if student1[2] != 'A' and student2[2] != 'A':
    print(None)
elif student1[2] != 'A':
    print('2A')
elif student2[2] != 'A':
    print('1A')
else:
    print('BOTH')