def sol(n, final):
    print(n)
    n -= 5
    if n == final:
        return
    if n > 0:
        return sol(n, final)
    if n < 0:
        print(n)
        n += 10
        return sol(n, final)


def sol2(n, final):
    print(n)
    if n < 0 or n == 0:
        sol3(n + 5, final)
        return
    sol2(n - 5, final)


def sol3(n, final):
    print(n)
    if n == final:
        return
    sol3(n + 5, final)


sol2(10, 10)
