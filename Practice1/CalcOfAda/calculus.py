import sys

values = list(map(int, input().split()[1:]))
differences = [values]
while len(set(differences[-1])) > 1:
    differences.append([differences[-1][n] - differences[-1][n-1] for n in range(1, len(differences[-1]))])

print(len(differences) - 1, sum([d[-1] for d in differences]))