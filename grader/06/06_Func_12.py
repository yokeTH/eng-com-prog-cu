def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(n):
    while True:
        n+=1
        if is_prime(n):
            break
    return n

def next_twin_prime(n):
    while True:
        a = next_prime(n)
        b = next_prime(a)
        if b - a == 2:
            break
        n = a
    return a, b

exec(input().strip())