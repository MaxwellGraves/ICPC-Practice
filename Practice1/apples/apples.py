r, c = map(int, input().split())

space = ['' for _ in range(c)]

for row in range(r):
    vals = input()
    for col in range(c):
        space[col] += vals[col]

new_space = []

for col in space:
    splits = col.split('#')
    splits = [''.join(sorted(s)) for s in splits]
    new_space.append('#'.join(splits))

for row in range(r):
    print(''.join([new_space[col][row] for col in range(c)]))
    