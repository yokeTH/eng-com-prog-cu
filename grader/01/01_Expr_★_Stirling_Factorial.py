import math

n = int(input())

base = math.sqrt(math.pi * 2) * n**(n + 0.5)

lowerBound = base * math.e**(-n + (1 / (12 * n + 1)))
upperBound = base * math.e**(-n + (1 / (12 * n)))

print(lowerBound)
print(upperBound)