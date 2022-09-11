mapping = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0',
}

n = int(input())
cases = [input() for _ in range(n)]
for j, case in enumerate(cases):
    ans = ''
    for i, char in enumerate(case[:-1]):
        ans += mapping[char]
        if mapping[case[i+1]][0] == ans[-1]: ans += ' '
    ans += mapping[case[-1]]
    print(f'Case #{j+1}: {ans}')
