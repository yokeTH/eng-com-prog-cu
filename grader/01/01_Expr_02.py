from math import sqrt

a,b,c = map(float,(input(),input(),input()))

discriminant = sqrt(b**2 - 4*a*c)
print(-b+discriminant)

print(round((-b-discriminant) / (2*a), 3),round((-b+discriminant) / (2*a), 3))