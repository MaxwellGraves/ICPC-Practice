diff = (-int(input())+int(input())) % 360
print(diff if diff <= abs(diff-360) else diff-360)