import random
from time import time


def is_sum(a, s, n):
    start = 0
    end = 1
    while sum(a[start:end]) != s:
        if sum(a[start:end]) < s:
            if end == n:
                print(-1)
                return
            end += 1
        elif sum(a[start:end]) > s:
            if end == n:
                print(-1)
                return
            start += 1
    print(start + 1, end, a[start:end])


def is_sum2(a, s, n):
    start = 0
    end = 1
    mysum = a[0]
    while mysum != s:
        if mysum < s:
            if end == n:
                print(-1)
                return
            mysum += a[end]
            end += 1
        elif mysum > s:
            if end == n:
                print(-1)
                return
            mysum -= a[start]
            start += 1
    print(start + 1, end, a[start:end])


n = 1000000
s = 1000001
numbers = []

t = time()
for i in range(n):
    numbers.append(random.randint(0, n + 1))
print('loop: ', time() - t)

t = time()
is_sum(numbers, s, n)
is_sum1_time = time() - t
print('is_sum1: ', is_sum1_time)
t = time()
is_sum2(numbers, s, n)
is_sum2_time = time() - t
print('is_sum2: ', is_sum2_time)

print(is_sum2_time / is_sum1_time)

# T = int(input())
# for test in range(T):
#     N = int(input())
#     s = int(input())
#     numbers = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#     subarray(numbers, s)
