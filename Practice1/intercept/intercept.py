from math import inf
import heapq as hq

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for edge in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((start, end, time))

start, end = map(int, input().split())

# Dijkstras

d = [inf for _ in range(n)]
d[start] = 0

edge_queue = [e[::-1] for e in graph[start]]
hq.heapify(edge_queue)

i = 0
    
while len(edge_queue):
    cost, e, s = hq.heappop(edge_queue)

    total_cost = cost + d[s]
    if total_cost < d[e]:
        d[e] = total_cost
        for edge in graph[e]:
            hq.heappush(edge_queue, edge[::-1])

reverse = [[] for _ in range(n)]

for start in range(n):
    for edge in graph[start]:
        reverse[edge[1]].append((edge[1], edge[0], edge[2]))

# Reverse BFS        
seen = set()
frontier = {end}
ans = []
while frontier:
    if len(frontier) == 1:
        ans.append(list((frontier))[0])
    new_frontier = set()
    for v in frontier:
        for edge in reverse[v]:
            s, e, c = edge
            if d[s] - c == d[e] and e not in seen:
                new_frontier.add(e)
                seen.add(e)
    frontier = new_frontier

print(' '.join(map(str, sorted(ans))))        
