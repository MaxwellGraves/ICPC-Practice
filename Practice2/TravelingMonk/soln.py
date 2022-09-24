from math import inf

def calc_line(curr_h, curr_t, dh, dt):
    y_int = curr_h - curr_t * (dh/dt)
    return (dh/dt, y_int)

def calc_int(line_a, line_b):
    if line_a[0] == line_b[0]:
        return -2 if line_a[1] == line_b[1] else -1
    return (line_b[1] - line_a[1])/(line_a[0] - line_b[0])

a, d = map(int, input().split())

a_segs = []
d_segs = [] 
for _ in range(a):
    a_segs.append(list(map(int, input().split())))

for _ in range(d):
    d_segs.append(list(map(int, input().split())))
    d_segs[-1][0] *= -1



total_height = sum([x[0] for x in a_segs])

ta, td = 0, 0
# Slope intercept form
line_d = (0, total_height) 
line_a = (0, 0)
i, j = 0, 0

while i < len(a_segs) or j < len(d_segs):
    if ta <= td:
        dh, dt = a_segs[i]
        i += 1
        curr_h = line_a[0]*ta + line_a[1]
        line_a = calc_line(curr_h, ta, dh, dt)
        int_time = calc_int(line_a, line_d)
        # print('a')
        # print(line_a ,line_d)
        # print(ta, td)
        # print(curr_h, int_time)
        # print()
        if ta <= int_time and int_time <= min(td, ta+dt):
            print(int_time)
            exit()
        elif int_time == -2:
            print(ta)
            exit()
        ta += dt
    elif ta > td:
        dh, dt = d_segs[j]
        j += 1
        curr_h = line_d[0]*td + line_d[1]
        line_d = calc_line(curr_h, td, dh, dt)
        
        int_time = calc_int(line_a, line_d)
        # print('d')
        # print(line_a ,line_d)
        # print(ta, td)
        # print(curr_h, int_time)
        # print()
        if td <= int_time and int_time <= min(ta, td+dt):
            print(int_time)
            exit()
        elif int_time == -2:
            print(td)
            exit()
        td += dt

