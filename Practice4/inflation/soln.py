n = int(input())
inflations = list(sorted(map(int, input().split())))

worst = 1
for i, gas in enumerate(inflations):
    i += 1
    if gas > i:
        print('impossible')
        quit()
    else:
        worst = min(worst, gas/i)
print(worst)
