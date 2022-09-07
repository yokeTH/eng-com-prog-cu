string = input()
ans = ''

for i in range(len(string)):
    if string[i] == '(':
        ans+= '['
    elif string[i] == '[':
        ans+= '('
    elif string[i] == ']':
        ans+= ')'
    elif string[i] == ')':
        ans+= ']'
    else:
        ans+= string[i]
        
print(ans)