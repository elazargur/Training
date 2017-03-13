
#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    orig = 'hackerrank'
    sub = []

    for letter in orig:
        for i, char in enumerate(s):
            if letter == char:
                s = s[i+1:]
                sub.append(char)
                break

    s = ''.join(sub)

    if s == orig:
        print('YES')
    else:
        print('NO')
