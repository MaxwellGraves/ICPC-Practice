# p = 998244353

# fac = [1]
# for i in range(1, p):
#     fac

# def height(m, n):


# print(height(2, 3))

import numpy as np
from math import pow

MOD = 998244353
dp = [0, 1]

for i in range(2, 80000 + 1):
    dp.append( (MOD - MOD // i) * dp[MOD % i] % MOD )

def height(n,m):
    h, t = 0, 1
    m %= MOD

    for i in range(1, n + 1): 
        t = t * (m - i + 1) * dp[i] % MOD
        h = (h + t) % MOD
    return h % MOD

first_ten = [[height(n, m) for n in range(12)] for m in range(12)]
print(np.array(first_ten))