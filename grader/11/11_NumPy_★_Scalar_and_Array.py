import numpy as np
def toCelsius( f ):
    return (f-32)/9*5
def BMI( wh ):
    return wh[:,0] / (wh[:,1]/100)**2
def distanceTo( p, Points ):
    return ((Points[:,0] - p[0])**2 + (Points[:,1] - p[1])**2)**0.5
exec(input().strip())