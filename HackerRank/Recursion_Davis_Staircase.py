

def climbing(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return climbing(n-3) + climbing(n-2) + climbing(n-1)


s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(n, '-->', climbing(n))
