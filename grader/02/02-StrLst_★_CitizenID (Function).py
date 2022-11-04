def check_digit(n:str):
    return (11 - sum( [i * v for i, v in enumerate(list(map(int, list(n)))[::-1], 2)]) % 11) % 10

exec(input())
