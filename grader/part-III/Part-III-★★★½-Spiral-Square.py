def boder(n,radius):
    n -= 1
    ans = []
    for i in range(n-radius,0+radius,-1):
        ans.append([n-radius,i])
    last = ans[-1]
    for i in range(n-radius,0+radius,-1):
        ans.append([i,last[1]-1])
    last = ans[-1]
    for i in range(0+radius,n-radius):
        ans.append([last[0]-1,i])
    last = ans[-1]
    for i in range(0+radius,n-radius):
        ans.append([i,last[1]+1])
    return ans

def spiral_square(n): # n is a positive odd number
    ringRadian = n//2
    counter = n*n
    s = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(ringRadian):
        for j in boder(n,i):
            s[j[0]][j[1]] = counter
            counter -= 1
    s[ringRadian][ringRadian] = 1
    return s

def print_square(S): #เรยีกใชฟ้ังกช์นันเี้พอื่แสดงคา่ของSทเี่ป็นลสิตข์องลสิตข์องจานวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())