from math import log, sqrt


w,h = map(float,(input(),input()))

print(sqrt(w*h)/60)
print(0.024265 * w**0.5378 * h**0.3964)
print(0.0333 * w**(0.6157-0.0188*log(w,10)) * h**0.3)