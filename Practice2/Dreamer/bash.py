from itertools import permutations

n = int(input())

cases = [input().replace(' ', '') for _ in range(n)]


def leap_year(year):
    if not year%400: return True
    if not year%100: return False
    if not year%4: return True
    return False

def check_if_valid_date(date):
    year = int(date[4:])
    if year < 2000: return False, (0, 0, 0)

    month = int(date[2:4])
    if month > 12 or month < 1: return False, (0, 0, 0)

    day = int(date[:2])
    if day > 31 or day < 1: return False, (0, 0, 0)

    if month in [2, 4, 6, 9, 11] and day > 30: return False, (0, 0, 0)

    if month == 2 and not leap_year(year) and day > 28: return False, (0, 0, 0)
    elif month == 2 and day > 29: return False, (0, 0, 0)

    return True, (year, month, day)

def solve(case):
    count = 0
    earliest = None
    seen = set()
    # print()
    for p in permutations(case):
        valid, date = check_if_valid_date(''.join(p))
        if valid and date not in seen:
            # print(date)
            seen.add(date)
            count += 1
            if not earliest or date < earliest:
                earliest = date

    print(count, end=' ')
    if count:
        print(' '.join(reversed([str(x).zfill(2) for x in earliest])), end='')
    print()

for case in cases:
    solve(case)



