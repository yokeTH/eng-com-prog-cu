from string import digits, ascii_letters
words = input()
ans = ''
cnt = 0
isValid = False
for i in words:
    if i in digits+ascii_letters:
        if isValid:
            ans += i.lower()
        else:
            if cnt == 0:
                ans+= i.lower()
            else:
                ans+= i.upper()
            cnt += 1
            isValid = True
    else:
        isValid = False

print(ans)