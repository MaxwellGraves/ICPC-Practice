from collections import deque
n, m = map(int, input().split())

adj = [[] for _ in range(n)]
in_deg = [0 for _ in range(n)]
for _ in range(m):
    top, bottom = map(int, input().split())
    adj[top-1].append(bottom-1)
    in_deg[bottom-1] += 1

ans = []
seen = set()
queue = [x for x in range(n) if in_deg[x] == 0]
size = len(queue)
queue = deque(queue)
while size:
    stick = queue[0]
    queue.popleft()
    size -= 1
    ans.append(stick)
    for bottom in adj[stick]:
        in_deg[bottom] -= 1
        if in_deg[bottom] == 0:
            size += 1
            queue.append(bottom)   

if len(ans) != n:
    print('IMPOSSIBLE')
else:
    print('\n'.join(map(str, map(lambda x: x + 1, ans))))