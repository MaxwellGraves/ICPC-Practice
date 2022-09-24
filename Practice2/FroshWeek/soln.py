n = int(input())
data = [int(input()) for _ in range(n)]

s = list(sorted(data))

ans = 0

def merge(data, a, b):
    inv_count = 0
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
            inv_count += len(a) - i

    if i < len(a):
        result.extend(a[i:])
    if j < len(b):
        result.extend(b[j:])
    data.append(result)
    return inv_count


data = [[n] for n in data]
while len(data) > 1:
    new_data = []
    num_of_subs = len(data)
    for i in range(num_of_subs//2):
        ans += merge(new_data, data[2*i], data[2*i + 1])
    if num_of_subs % 2 == 1:
        new_data.append(data[-1])
    data = new_data
    
print(ans)

