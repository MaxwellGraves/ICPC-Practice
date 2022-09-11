n = int(input())
stack = []
code = input()
for i, l in enumerate(code):
    if l in "[{(":
        stack.append(l)
    elif l in "]})":
        if not stack:
            print(l + " " + str(i))
            quit()
        prev = stack.pop()
        if prev == '{' and l != '}' \
        or prev == '[' and l != ']' \
        or prev == '(' and l != ')':
            print(l + " " + str(i))
            quit()
print('ok so far')