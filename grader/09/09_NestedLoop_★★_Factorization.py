def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def nextPrime(n):
    while True:
        n+=1
        if isPrime(n):
            break
    return n

def factor(n):
    ans = []
    prime = 2
    cnt = 0
    while n!=1:
        if n%prime == 0:
            cnt+=1
            n/=prime
        else:
            if cnt!=0:
                ans.append([prime,cnt])
            cnt = 0
            prime = nextPrime(prime)
    ans.append([prime,cnt])
    return ans

exec(input().strip())