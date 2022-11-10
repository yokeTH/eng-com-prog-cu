def knows(R,x,y):
    if y in R[x]:
        return True
    return False

def is_celeb(R,x):
    for k in R:
        if k != x and x not in R[k]:
            return False
    if len(R[x] - {x}) == 0:
        return True
    return False

def find_celeb(R):
    for e in R:
        if is_celeb(R,e):
            return e

def read_relations() :
    R = {}
    while True:
        d = input().split()
        if len(d) == 1: break
        if d[0] in R:
            R[d[0]].add(d[1])
        else:
            R[d[0]] = {d[1]}
        if not d[1] in R:
            R[d[1]] = set()
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)

exec(input())