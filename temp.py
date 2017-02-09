

d = {'[': ']', '{': '}', '(': ')'}

def is_matched(expression):
    l = []
    if len(expression) % 2 != 0:
        return False
    for b in expression:
        if b not in d:
            break
        l.append(d[b])
    l.reverse()
    check = ''.join(l)
    if check == expression[int(len(expression) / 2):]:
        return True
    return False


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
