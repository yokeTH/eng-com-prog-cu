from string import ascii_uppercase
ln = input()

while ln.lower() != 'end':
    lnOut = ''
    for i in ln:
        if i.isupper():
            lnOut += ascii_uppercase[(ascii_uppercase.find(i.upper()) + 13)%26]
        elif i.islower():
            lnOut += ascii_uppercase[(ascii_uppercase.find(i.upper()) + 13)%26].lower()
        else:
            lnOut += i
    print(lnOut)
    ln = input()