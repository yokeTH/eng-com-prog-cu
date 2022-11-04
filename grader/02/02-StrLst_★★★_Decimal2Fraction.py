import math
import numpy as np

a,b,c = input().split(',')

sed = (int(b+c) - int('0'+b))
suan = int('9'*len(c) + '0'*len(b))

sed2 = suan * int(a) + sed
gcd = math.gcd(sed2,suan)


print('{} / {}'.format(int(sed2/gcd),int(suan/gcd)))