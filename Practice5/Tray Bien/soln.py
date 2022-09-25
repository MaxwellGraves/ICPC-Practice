from math import floor

m, n = map(int, input().split())

b = list(map(lambda x: floor(float(x)), input().split()))

bad_spots = {(b[2*x+1], b[2*x]) for x in range(len(b)//2)}

top_down = [[0] * m for _ in range(3)]
bot_up = [[0] * m for _ in range(3)]
t = [0] * m
c = [0] * m

# Setup top_down
for i in range(3):
    if i == 0:
        top_down[i][0] = 1
        continue
    top_down[i][0] = top_down[i-1][0]
    if (i, 0) not in bad_spots and (i-1, 0) not in bad_spots:
        top_down[i][0] += 1 if i < 2 else top_down[i-2][0]

# Setup bot_up
for i in reversed(range(3)):
    if i == 2:
        bot_up[i][0] = 1
        continue
    bot_up[i][0] = bot_up[i+1][0]
    if (i, 0) not in bad_spots and (i+1, 0) not in bad_spots:
        bot_up[i][0] += 1 if i != 0 else bot_up[i+2][0]

# Setup T & C
t[0] = 1
c[0] = 1

for col in range(1, m):
    # Top Down 0
    top_down[0][col] = top_down[2][col-1]
    if (0, col) not in bad_spots and (0, col-1) not in bad_spots:
        top_down[0][col] += bot_up[1][col-1]
    
    # Top Down 1
    top_down[1][col] = top_down[0][col]
    if (1, col) not in bad_spots:
        if (0, col) not in bad_spots:
            top_down[1][col] += top_down[2][col-1]
        if (1, col-1) not in bad_spots:
            top_down[1][col] += c[col-1]
            if (0, col) not in bad_spots and (0, col-1) not in bad_spots:
                top_down[1][col] += bot_up[2][col-1]
    
    # Top Down 2
    top_down[2][col] = top_down[1][col]
    if (2, col) not in bad_spots:
        if (1, col) not in bad_spots:
            top_down[2][col] += top_down[0][col]
        if (2, col-1) not in bad_spots:
            top_down[2][col] += top_down[1][col-1]
            if (0, col) not in bad_spots and (1, col) not in bad_spots:
                top_down[2][col] += top_down[1][col-1]
            if (0, col) not in bad_spots and (0, col-1) not in bad_spots and (1, col) not in bad_spots and (1, col-1) not in bad_spots:
                top_down[2][col] += top_down[2][col-2] if col > 1 else 1
            if (0, col) not in bad_spots and (0, col-1) not in bad_spots:
                top_down[2][col] += t[col-1]
            if (1, col) not in bad_spots and (1, col-1) not in bad_spots:
                top_down[2][col] += top_down[0][col-1]
    
    # Bottom Up 2
    bot_up[2][col] = bot_up[0][col-1]
    if (2, col) not in bad_spots and (2, col-1) not in bad_spots:
        bot_up[2][col] += top_down[1][col-1]

    # Bottom Up 1
    bot_up[1][col] = bot_up[2][col]
    if (1, col) not in bad_spots:
        if (2, col) not in bad_spots:
            bot_up[1][col] += bot_up[0][col-1]
        if (1, col-1) not in bad_spots:
            bot_up[1][col] += c[col-1]
            if (2, col) not in bad_spots and (2, col-1) not in bad_spots:
                bot_up[1][col] += top_down[0][col-1]
    
    # Bottom Up 0
    bot_up[0][col] = bot_up[1][col]
    if (0, col) not in bad_spots:
        if (1, col) not in bad_spots:
            bot_up[0][col] += bot_up[2][col]
        if (0, col-1) not in bad_spots:
            bot_up[0][col] += bot_up[1][col-1]
            if (1, col) not in bad_spots and (2, col) not in bad_spots:
                bot_up[0][col] += bot_up[1][col-1]
            if (1, col) not in bad_spots and (1, col-1) not in bad_spots and (2, col) not in bad_spots and (2, col-1) not in bad_spots:
                bot_up[0][col] += bot_up[0][col-2] if col > 1 else 1
            if (1, col) not in bad_spots and (1, col-1) not in bad_spots:
                bot_up[0][col] += bot_up[2][col-1]
            if (2, col) not in bad_spots and (2, col-1) not in bad_spots:
                bot_up[0][col] += t[col-1]
    # T
    t[col] = top_down[2][col-1]
    if (1, col) not in bad_spots and (1, col-1) not in bad_spots:
        t[col] += c[col-1]

    # C
    c[col] = top_down[2][col-1]
    if (0, col) not in bad_spots and (0, col-1) not in bad_spots and (2, col) not in bad_spots and (2, col-1) not in bad_spots:
        c[col] += t[col-1]
    if (0, col) not in bad_spots and (0, col-1) not in bad_spots:
        c[col] += bot_up[1][col-1]
    if (2, col) not in bad_spots and (2, col-1) not in bad_spots:
        c[col] += top_down[1][col-1]

print(top_down[-1][-1])

# Debug Prints
# from numpy import array as a
# print(a(top_down))
# print(a(bot_up))
# print(t)
# print(c)
# print(bad_spots)