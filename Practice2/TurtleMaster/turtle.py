grid = [[*input()] for _ in range(8)]
program = input()

def check_inside(pos):
    return pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8

turtley, turtlex = 7, 0
facing = 1 # 0 is north, +1 clockwise

grid[turtley][turtlex] = '.'

for inst in program:
    # print(turtley, turtlex + 1)
    # print(check_inside((turtley, turtlex + 1)))
    # print(grid[turtley][turtlex + 1])
    # print(facing)
    if inst == 'F':
        if facing == 0 and check_inside((turtley - 1, turtlex)) and grid[turtley - 1][turtlex] in 'D.': turtley -= 1
        elif facing == 1 and check_inside((turtley, turtlex + 1)) and grid[turtley][turtlex + 1] in 'D.': turtlex += 1
        elif facing == 2 and check_inside((turtley + 1, turtlex)) and grid[turtley + 1][turtlex] in 'D.': turtley += 1
        elif facing == 3 and check_inside((turtley, turtlex - 1)) and grid[turtley][turtlex - 1] in 'D.': turtlex -= 1
        else:
            print('Bug!')
            exit()
    elif inst == 'R':
        facing += 1
        facing %= 4
    elif inst == 'L':
        facing -= 1
        facing %= 4
    elif inst == 'X':
        if facing == 0 and check_inside((turtley - 1, turtlex)) and grid[turtley - 1][turtlex] == 'I': grid[turtley - 1][turtlex] = '.'
        elif facing == 1 and check_inside((turtley, turtlex + 1)) and grid[turtley][turtlex + 1] == 'I': grid[turtley][turtlex + 1] = '.'
        elif facing == 2 and check_inside((turtley + 1, turtlex)) and grid[turtley + 1][turtlex] == 'I': grid[turtley + 1][turtlex] = '.'
        elif facing == 3 and check_inside((turtley, turtlex - 1)) and grid[turtley][turtlex - 1] == 'I': grid[turtley][turtlex - 1] = '.'
        else: 
            print('Bug!')
            exit()

if grid[turtley][turtlex] == 'D':
    print('Diamond!')
else:
    print('Bug!')

