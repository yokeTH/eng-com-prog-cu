import numpy as np
from math import e

def p( X ):
    return 1 / (1 + e**-(-3.98 + 0.1*X[:,0] + 0.5*X[:,1]))

exec(input().strip())