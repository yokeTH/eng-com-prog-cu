def findNextTo(helix:str, pattern):
    cnt = 0
    if helix[-1].upper() not in ['A','T','C','G']:
            return 'Invalid DNA'
    for i in range(len(helix)-1):
        if helix[i].upper() not in ['A','T','C','G']:
            return 'Invalid DNA'
        if helix[i:i+2].upper() == pattern.upper():
            cnt+=1
    return cnt

def count(helix:str):
    cnts = [0,0,0,0]
    for i in helix:
        i = i.upper()
        if i == 'A':
            cnts[0] += 1
        elif i == 'T':
            cnts[1] += 1
        elif i == 'G':
            cnts[2] += 1
        elif i == 'C':
            cnts[3] += 1
        else:
            return 'Invalid DNA'
    return 'A={0[0]}, T={0[1]}, G={0[2]}, C={0[3]}'.format(cnts)

def reverse(helix:str):
    ans = ''
    for i in helix:
        i = i.upper()
        if i == 'A':
            ans+= 'T'
        elif i == 'T':
            ans+= 'A'
        elif i == 'G':
            ans+= 'C'
        elif i == 'C':
            ans+= 'G'
        else:
            return 'Invalid DNA'
    return ans[::-1]

# ----------

helix = input().strip()
opt = input()
if opt == 'R':
    print(reverse(helix))
elif opt == 'F':
    print(count(helix))
else:
    print(findNextTo(helix,input()))