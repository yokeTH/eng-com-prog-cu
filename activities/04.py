import string

out = ''

for i in input():
    if i in string.ascii_letters:
        out += '*'
    elif i in string.digits:
        out += '#'
    else:
        out += i

print(out)