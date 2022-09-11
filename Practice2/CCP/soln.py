import math

def round_half_up(x):
    return math.floor(x + 0.5)

n = int(input())
for _ in range(n):
    r, b, m = map(int, [s.replace('.', '') for s in input().split()])
    r /= 100
    c = 0
    while b > 0 and c <= 1200:
        i = r*b / 100
        b += round_half_up(i) - m
        c += 1
    
    print(c if c <= 1200 else 'impossible')