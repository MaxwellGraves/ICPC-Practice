import heapq as hq
from math import inf
from collections import deque

def find(x, a):
    if a == x[a]:
        return a
    ret_val = find(x, x[a])
    x[a] = ret_val
    return ret_val

def union(x, a, b):
    if x[a] != x[b]:
        x[find(x, a)] = x[find(x, b)]
        

n, m, p = map(int, input().split())
edges = []

p_s = set(map(lambda x: int(x) - 1, input().split()))
for i in range(m):
    s, e, c = map(int, input().split())
    edges.append((c, s-1, e-1))

if n == 2 and p == 2 and m ==1:
    print(edges[0][0])
    quit()

edges.sort()

x = [a for a in range(n)] 

total_cost = 0
for c, s, e in edges:
    if s in p_s and e in p_s:
        continue
    if e in p_s:
        s, e = e, s
    if s in p_s and x[s] == s:
        union(x, s, e)
        total_cost += c
    elif s not in p_s and find(x, s) != find(x, e):
        union(x, s, e)
        total_cost += c
leader_count = 0
for i, v in enumerate(x):
    if i == v:
        leader_count += 1
print(total_cost if leader_count == 1 else 'impossible')
