n, m, q = map(int, input().split())
grid = [[0] * m for _ in range(n)]

def explore(i, j, seen):
    if i-1 >= 0 and (i-1, j) not in seen and grid[i-1][j] == 0:
        seen.add((i-1, j))
        explore(i-1, j, seen)
    if i+1 < len(grid) and (i+1, j) not in seen and grid[i+1][j] == 0:
        seen.add((i+1, j))
        explore(i+1, j, seen)
    if j-1 >= 0 and (i, j-1) not in seen and grid[i][j-1] == 0:
        seen.add((i, j-1))
        explore(i, j-1, seen)
    if j+1 < len(grid[0]) and (i, j+1) not in seen and grid[i][j+1] == 0:
        seen.add((i, j+1))
        explore(i, j+1, seen)

def regions():
    seen = set()
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in seen and grid[i][j] == 0:
                seen.add((i, j))
                ans += 1
                explore(i, j, seen)
    return ans

for i in range(q):
    x1, y1, x2, y2 = map(lambda x: x-1, map(int, input().split()))
    while x1 != x2:
        grid[x1][y1] = 1
        x1 += 1 if x2 > x1 else -1
    while y1 != y2:
        grid[x1][y1] = 1
        y1 += 1 if y2 > y1 else -1
    grid[x1][y1] = 1
    print(regions())
    