from math import sqrt, inf

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((y2-y1)**2+(x2-x1)**2)

def distance_p(a_line, b_line, dt):
    x1a, y1a, dxa, dya, dta = a_line
    x1b, y1b, dxb, dyb, dtb = b_line
    x1, y1, = x1a + dxa * dt/dta, y1a + dya * dt/dta
    x2, y2, = x1b + dxb * dt/dtb, y1b + dyb * dt/dtb
    return distance((x1, y1), (x2, y2))

def add_time(a_segs):
    for i, seg in enumerate(a_segs):
        x, y = seg
        if i == 0:
            a_segs[i] = (x, y, 0.0)
        else:
            px, py, pt = a_segs[i-1]
            a_segs[i] = (x, y, pt + distance((x, y), (px,py)))

def calc_min_dist(a_line, b_line, start_t):
    if not a_line or not b_line: return inf
    x1a, y1a, dxa, dya, dta = a_line
    x1b, y1b, dxb, dyb, dtb = b_line
    end_t = start_t + min(dta, dtb)

    print(a_line, b_line, start_t, end_t)

    denominator = ((dxb/dtb)-(dxa/dta))**2 + ((dyb/dtb) - (dya/dta))**2
    if denominator != 0: 
        numerator = -((x1b-x1a) * ((dxb/dtb)-(dxa/dta)) + (y1b-y1a) * ((dyb/dtb) - (dya/dta)))
        closest_time = numerator / denominator
    else:
        closest_time = start_t
    
    if closest_time >= start_t and closest_time <= end_t:
        return distance_p(a_line, b_line, closest_time-start_t)
    else:
        print(distance_p(a_line, b_line, 0), distance_p(a_line, b_line, end_t-start_t))
        return min(distance_p(a_line, b_line, 0), distance_p(a_line, b_line, end_t-start_t))

n = int(input())
a_segs = [tuple(map(int, input().split())) for _ in range(n)]
add_time(a_segs)
a_segs = list(reversed(a_segs))

m = int(input())
b_segs = [tuple(map(int, input().split())) for _ in range(m)]
add_time(b_segs)
b_segs = list(reversed(b_segs))

# print(a_segs, b_segs)

a_t, b_t = 0, 0
# Line: (x1, y1, deltax, deltay, deltaT)
a_line = None
b_line = None
min_dist = inf

while a_segs or b_segs:
    print()
    if (a_segs and b_segs and a_segs[-1][-1] < b_segs[-1][-1]) or (not b_segs):
        a_seg = a_segs.pop()
        x, y, t = a_seg
        if not a_line:
            a_line = (x, y, 0, 0, t)
        else:
            px, py, pdx, pdy, pt = a_line
            a_line = (px+pdx, py+pdy, x-(px+pdx), y-(py+pdy), t-pt)
            if b_line[-1]:
                print(calc_min_dist(a_line, b_line, a_t))
                min_dist = min(min_dist, calc_min_dist(a_line, b_line, a_t))
            a_t = t
    else:
        b_seg = b_segs.pop()
        x, y, t = b_seg
        if not b_line:
            b_line = (x, y, 0, 0, t)
        else:
            px, py, pdx, pdy, pt = b_line
            b_line = (px+pdx, py+pdy, x-(px+pdx), y-(py+pdy), t-pt)
            if a_line[-1]:
                print(calc_min_dist(a_line, b_line, b_t))
                min_dist = min(min_dist, calc_min_dist(a_line, b_line, b_t))
            b_t = t
print(min_dist)

