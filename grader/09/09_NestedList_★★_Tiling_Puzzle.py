def row_number(t, e):
    for row in range(len(t)):
        for ele in t[row]:
            if ele == e:
                return row
    return -1
def flatten(t):
    ans = []
    for i in t:
        for j in i:
            if j != 0:
                ans.append(j)
    return ans

def inversions(x):
    cnt = 0
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i] > x[j]:
                cnt += 1
    return cnt

def solvable(t):
    if len(t)%2 == 1 and inversions(flatten(t))%2 == 0:
        return True
    elif len(t)%2 == 0 and inversions(flatten(t))%2 == 1 and row_number(t,0) % 2 == 0:
        return True
    elif len(t)%2 == 0 and inversions(flatten(t))%2 == 0 and row_number(t,0) % 2 == 1:
        return True
    else:
        return False

exec(input().strip()) # do not remove this 