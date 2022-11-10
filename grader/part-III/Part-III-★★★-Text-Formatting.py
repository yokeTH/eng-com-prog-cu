data = open(input()).read().replace('\n','.').split('.')

k = int(input())
ruler = ''
for i in range(k//10):
    ruler += '-' * (10-len(str(i))) + str(i+1)
ruler += '-' * (k%10)
print(ruler)

ln = ''
for i in range(len(data)):
    if len(ln) + len(data[i]) < k:
        ln+=data[i]+'.'
    else:
        if ln.strip('.') != '':
            print(ln.strip('.'))
        ln = data[i]+'.'
print(ln.strip('.'))