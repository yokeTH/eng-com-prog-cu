A = input().split()
B = input().split()

if (A[2] != 'A' and A[3] < 'D' and A[4] < 'D') or (B[2] != 'A' and B[3] < 'D' and B[4] < 'D'):
    print(None)
elif A[2] != 'A':
    print(B[0])
elif B[2] != 'A':
    print(A[0])
elif float(A[1]) > float(B[1]):
    print(A[0])
elif float(A[1]) < float(B[1]):
    print(B[0])
elif A[3] < B[3]:
    print(A[0])
elif A[3] > B[3]:
    print(B[0])
elif A[4] < B[4]:
    print(A[0])
elif A[4] > B[4]:
    print(B[0])
else:
    print('BOTH')