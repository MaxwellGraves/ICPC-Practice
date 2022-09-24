n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
rings = [[0] * m for _ in range(n) ]

def neighbors(i, j):
    if i > 0:
        yield i-1, j
    if i < n-1:
        yield i+1, j
    if j > 0:
        yield i, j-1
    if j < m-1:
        yield i, j+1

queue = []
one_queue = []
seen  = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            rings[i][j] = 0
            point = (i, j)
            seen.add(point)
            queue.append(point)
        elif i == 0 or j == 0 or i == n-1 or j == m-1:
            rings[i][j] = 1
            point = (i, j)
            seen.add(point)
            one_queue.append(point)

ring_num = 0
while queue or one_queue:
    ring_num += 1
    new_queue = []
    for i, j in queue:
        for i_2, j_2 in neighbors(i, j):
            if (i_2, j_2) not in seen and grid[i_2][j_2] == 'T':
                rings[i_2][j_2] = ring_num
                point = (i_2, j_2)
                new_queue.append(point)
                seen.add(point)
    queue = new_queue
    if ring_num == 1:
        queue.extend(one_queue)
        one_queue = None
if ring_num < 10:
    for i in range(n):
        for ring_num in rings[i]:
            ring_num = int(ring_num)
            if ring_num == 0:
                print('..', end='')
            else:
                print(f'.{ring_num}', end='')
        print()
else:
    for i in range(n):
        for ring_num in rings[i]:
            ring_num = int(ring_num)
            if ring_num == 0:
                print('...', end='')
            elif ring_num >= 10:
                print(f'.{ring_num}', end = '')
            else:
                print(f'..{ring_num}', end='')
        print()

# for i in range(n):
#     for j in range(m):
#         if rings[i][j] != 0 and rings[i][j] - 1 not in map(lambda x:rings[x[0]][x[1]], neighbors(i, j)):
#             print(i, j, "SHEEET")
#             quit()

