r, c, n, m = map(int, input().split())

d_set = list(map(int,  input().split()))
d_set = {(d_set[2*x], d_set[2*x+1]) for x in range(len(d_set)//2)}\

k_set = list(map(int,  input().split()))
k_set = {(k_set[2*x], k_set[2*x+1]) for x in range(len(k_set)//2)}

print(d_set)
print(k_set)