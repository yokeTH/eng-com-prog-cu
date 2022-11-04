from math import sqrt


def sqrt_n_times(x, n):
    for _ in range(n): x = sqrt(x)
    return x

def cube_root(y):
    # prev = sqrt_n_times(y,2)
    # for i in range(1,6):
    #     now = prev * sqrt_n_times(prev,2**(i))
    #     prev = now
    #     print(2**(i))
    # return now

    # x1 = sqrt_n_times(y,2)
    # x2 = x1*sqrt_n_times(x1,2)
    # x3 = x2*sqrt_n_times(x2,4)
    # x4 = x3*sqrt_n_times(x3,8)
    # x5 = x4*sqrt_n_times(x4,16)
    # x6 = x5*sqrt_n_times(x5,32)
    # return x6

    # return y ** (  (1/4) * (1+1/4) * (1+1/16) * (1+1/2**8) * (1+1/2**16) * (1+1/2**32)  )
    pass

def main():
    q = float(input())
    print(cube_root(q))

exec(input())