nums = list(sorted(map(int, input().split())))
ans = []
for l in input():
    if l == 'A': ans.append(str(nums[0]))
    if l == 'B': ans.append(str(nums[1]))
    if l == 'C': ans.append(str(nums[2]))
print(' '.join(ans))
