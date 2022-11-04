num, digit = input(), int(input())

while len(num) < digit:
    num = '0' + num

print(num)