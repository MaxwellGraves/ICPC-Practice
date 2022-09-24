n = int(input())

starting_vals = input().split()
starting_vals = [False if l == 'F' else True for l in starting_vals]

eq = input().split()

stack = []

for char in eq:
    if char in '+*':
        op1, op2 = stack.pop(), stack.pop()
        if char == '+':
            stack.append(op1 or op2)
        elif char == '*':
            stack.append(op1 and op2)

    elif char == '-':
        op1 = stack.pop()
        stack.append(not op1)

    else:
        stack.append(starting_vals[ord(char) - ord('A')])

print('T' if stack.pop() else 'F')
