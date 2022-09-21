n, d = map(int, input().split())
costs = list(map(int, input().split()))

def _round(x):
    if x % 10 == 5:
        return x + 5
    else: return round(x, -1)

prev = {d:0}

# print(costs)

for c in costs:
    # print(prev)
    curr = {}
    for d_remaining, cost in prev.items():
        new_cost_w_d = _round(cost + c)
        if d_remaining:
            if d_remaining - 1 not in curr or new_cost_w_d < curr[d_remaining - 1]:
                curr[d_remaining - 1] = new_cost_w_d
            curr[d_remaining] = cost + c
        else:
            curr[0] = cost + c
    prev = curr

print(_round(min([x[1] for x in prev.items()])))