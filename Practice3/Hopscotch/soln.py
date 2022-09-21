n, x, y = map(int, input().split())

tot = 0
p = 10**9 + 7

for m in range(n//max(x, y)):
    balls = n - m*x
    