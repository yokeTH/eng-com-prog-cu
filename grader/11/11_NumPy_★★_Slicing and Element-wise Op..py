import numpy as np

def sum_2_rows( M ):
    return M[::2] + M[1::2]

def sum_left_right( M ):
    return M[:,:int(M.shape[1]/2)] + M[:,int(M.shape[1]/2):]

def sum_upper_lower( M ):
    return M[:int(M.shape[1]/2),:] + M[int(M.shape[1]/2):,:]

def sum_4_quadrants( M ):
    return M[:int(M.shape[1]/2),:int(M.shape[1]/2)] + M[int(M.shape[1]/2):,:int(M.shape[1]/2)] + M[:int(M.shape[1]/2),int(M.shape[1]/2):] + M[int(M.shape[1]/2):,int(M.shape[1]/2):]

def sum_4_cells( M ):
    return M[::2,::2] + M[1::2,::2] + M[::2,1::2] + M[1::2,1::2]

def count_leap_years( years ):
    years -= 543
    a = years % 400 == 0
    b = years % 100 != 0
    c = years % 4 == 0
    return (a | b & c).sum()
exec(input())