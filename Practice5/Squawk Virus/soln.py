n, m, s, t = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

infected = {s: 1}

for _ in range(t):
    # print(infected)
    new_infected = {}
    for source, s_count in infected.items():
        for neighbor in adj[source]:
            if neighbor not in new_infected: new_infected[neighbor] = 0
            new_infected[neighbor] += s_count
    infected = new_infected

print(sum(infected.values()))