from cProfile import run


values = [-1 if l == 'B' else 1 for l in input()]
runnin_sum = [0]
for v in values:
    runnin_sum.append(runnin_sum[-1] + v)
min_i, max_i = runnin_sum.index(min(runnin_sum)), runnin_sum.index(max(runnin_sum))

if min_i > max_i:
    min_i, max_i = max_i, min_i

print(min_i + 1, max_i)