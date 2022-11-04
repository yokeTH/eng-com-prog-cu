from math import factorial, log, pi, radians, sin, sqrt


ex1 = pi - (factorial(10)/8**8)
ex2 = log(9.7) ** ((7/sqrt(71))-sin(radians(40)))
ex3 = 1.2**(2.3**(1/3))

print(round((ex1+ex2)/ex3,6))