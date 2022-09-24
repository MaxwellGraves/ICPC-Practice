from math import floor
import numpy as np

m, n = map(int, input().split())

b = list(map(lambda x: floor(float(x)), input().split()))

bad_spots = {(b[2*x], b[2*x+1]) for x in range(len(b)//2)}

grid = np.array([[0 if (i, j) not in bad_spots else 1 for j in range(m)] for i in range(3)])

def neighbors(i, j):
    if i > 0:
        yield i-1, j
    if i < n-1:
        yield i+1, j
    if j > 0:
        yield i, j-1
    if j < m-1:
        yield i, j+1

def find_next_zero(grid, i, j):
    for n_j in range(j, m):
        for n_i in range(3):
            if grid[n_i][n_j] == 0:
                return n_i, n_j
    return -1, -1

def backtrack(grid, i, j):
    # print(grid, end='\n\n')
    n_i, n_j = find_next_zero(grid, i, j)
    if n_i == -1 and n_j == -1:
        return 1

    ans = 0
    grid[n_i][n_j] = 1
    for x, y in neighbors(n_i, n_j):
        if grid[x][y] == 0:
            grid[x][y] = 1
            ans += backtrack(grid, n_i, n_j)
            grid[x][y] = 0
    ans += backtrack(grid, n_i, n_j)
    grid[n_i][n_j] = 0
    return ans


print(backtrack(grid, 0, 0))