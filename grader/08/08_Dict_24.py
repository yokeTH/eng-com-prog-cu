from string import ascii_lowercase

keyText = {'0': ' '}
fourKey = [5,7]
cnt = 0
for i in range(8):
    keyText[str(i+2)] = ascii_lowercase[cnt]
    cnt+=1
    keyText[str(i+2)*2] = ascii_lowercase[cnt]
    cnt+=1
    keyText[str(i+2)*3] = ascii_lowercase[cnt]
    cnt+=1
    if i in fourKey:
        keyText[str(i+2)*4] = ascii_lowercase[cnt]
        cnt+=1

textKey = {}
for k in keyText:
    textKey[keyText[k]] = k



def text2keys( text ):
    s = ''
    for e in text:
        if e.lower() in textKey:
            s+=textKey[e.lower()]+' '
    return s.strip()

def keys2text( keys ):
    s = ''
    for e in keys.split():
        s+=keyText[e]
    return s.strip()

exec(input().strip())