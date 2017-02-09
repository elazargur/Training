"""for every char check if the matching one showed in expression[1:]
either recursively or iterative"""

d = {'[': ']', '{': '}', '(': ')'}


def is_matched(expression):
    l = list(expression)
    for b in expression:
        if b in d:
            l.remove(b)
            if d[b] in l:
                l.remove(d[b])
            else:
                return False
    if len(l) == 0:
        return True
    return False


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
