# 2565_1_Quiz_1_2.py

def f1(a, b, c):
    x = [a,b,c]
    if a <= 0:
        x.remove(a)
    if b <= 0:
        x.remove(b)
    if c <= 0:
        x.remove(c)
    return  int(min(x))

def f2(a, b, c):
    x = [a,b,c]
    if a >= 0:
        x.remove(a)
    if b >= 0:
        x.remove(b)
    if c >= 0:
        x.remove(c)
    return  int(max(x))
    
def f3(a, b, c):
    return  int(str(abs(a+b+c))[0])
    
def f4(a, b, c):
    return  int(str(abs(a+b+c))[-1])
    
def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a,b,c))
    elif s1 == 0 and s2 == 1:
        print(f2(a,b,c))
    elif s1 == 1 and s2 == 0:
        print(f3(a,b,c))
    elif s1 == 1 and s2 == 1:
        print(f4(a,b,c))
    else:
        print('Error')

exec(input().strip())
