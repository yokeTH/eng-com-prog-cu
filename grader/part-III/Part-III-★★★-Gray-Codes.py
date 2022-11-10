def gray(n):
    if n == 1:
        return ['0','1']
    else:
        return ['0'+a for a in gray(n-1)] + ['1'+a for a in gray(n-1)[::-1]]

n,k = int(input()), int(input())

if n < 0 and k < 0:
    print('Invalid n and k')
elif n < 0:
    print('Invalid n')
elif k < 0:
    print('Invalid k')
else:
    code = gray(n)
    ln = ''

    for i in range(1,k+1):
        ln+= str(i) + '-'*(n+1 - len(str(i)))
    print(ln[:-1])

    for i in range(0,len(code),k):
        print(','.join(code[i:i+k]))