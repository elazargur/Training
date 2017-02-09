# n = int(input())
# numbers = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def fibo(n):
    print(n)
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)


def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


def fibo2(n):
    a = 1
    b = 1
    print('{}\n{}'.format(a, b))
    while b < 100:
        c = a + b
        print(c)
        a = b
        b = c


cache = {}


def decode(s):
    if s in cache:
        return cache[s]
    if len(s) == 0:
        return 1
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    if int(s[:2]) <= 26:
        ways = decode(s[1:]) + decode(s[2:])
    else:
        ways = decode(s[1:])
    cache[s] = ways
    return ways


T = int(input())

def split_string(s):
    even = [c for i, c in enumerate(s) if i % 2 == 0]
    odd = [c for i, c in enumerate(s) if i % 2 != 0]
    print('{} {}'.format(''.join(even), ''.join(odd))


