def blackWhite(row:str,col:int):
    return 'Black' if (ord(row) + col)%2 else 'White'

s = input()
if len(s) > 3:
    s = s.split(',')

    if 'row' in s[0]:
        row = s[0].split('=')[1].strip()
        col = s[1].split('=')[1].strip()
    else:
        row = s[1].split('=')[1].strip()
        col = s[0].split('=')[1].strip()

else:
    row = s[0]
    col = s[1:].strip()
print('|{}|'.format(row))
print('|{}|'.format(col))
validRow = len(row) == 1 and ('A' <= row <= 'Z' or 'a' <= row <= 'z')
validCol = col.isdigit() and 1 <= int(col) <= 52

if not validRow and not validCol:
    print('Invalid row and column')
elif not validRow:
    print('Invalid row')
elif not validCol:
    print('Invalid column')
else:
    print(blackWhite(row, int(col)))