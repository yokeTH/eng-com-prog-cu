word = input()

if word.endswith(('s', 'x', 'ch')):
    word += 'es'
elif word.endswith('y') and word[-2] not in ['a','e','i','o','u']:
    word = word[:-1]
    word += 'ies'
else:
    word+='s'

print(word)