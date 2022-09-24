from random import random
print(100, 100)
for _ in range(100):
    for _ in range(100):
        print('.' if random() >= 0.999 else 'T', end = '')
        # print('T', end = '')

    print()