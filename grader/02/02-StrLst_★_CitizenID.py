digits = input('Citizen ID: ')
lastDigit = (11 - sum( [i * v for i, v in enumerate(list(map(int, list(digits)))[::-1], 2)]) % 11) % 10
print(digits[0], digits[1:5], digits[5:10], digits[10:12], lastDigit)