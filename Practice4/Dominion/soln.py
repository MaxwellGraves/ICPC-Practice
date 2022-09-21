g, s, c = map(int, input().split())
total_gold = 3*g + 2*s + c

ans = []
if total_gold >= 8:
    ans.append('Province')
elif total_gold >= 5:
    ans.append('Duchy')
elif total_gold >= 2:
    ans.append('Estate')

if total_gold >= 6: 
    ans.append('Gold')
elif total_gold >= 3: 
    ans.append('Silver')
else:
    ans.append('Copper')

print(' or '.join(ans))