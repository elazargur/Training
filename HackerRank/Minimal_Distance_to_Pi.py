#
# import math
# # input: min, max 221014255319169 221014935871432
#
# def get_frac(d):
#     l = []
#     n = math.floor(d * math.pi)  # floor
#     o1 = abs(n / d - math.pi)
#     o2 = abs((n + 1) / d - math.pi)
#     if not o1 < o2:
#         l = [d, n + 1, o2]
#         return l
#     l = [d, n, o1]
#     return l
#
# min = [0, 0, 1]
# for i in range(221014255319169, 221014255319180):
#     l = get_frac(i)
#     if l[2] < min[2]:
#         min = l
#
# print('{}/{}'.format(min[1], min[0]))
# print(min)

import decimal

decimal.getcontext().prec = 50

pi = decimal.Decimal(31415926535897932384626433832795028841971693993751) / 10 ** 49


def getNumerator(denominator):
    return int(denominator * pi + decimal.Decimal(0.5))


def getDistanceToPi(denominator):
    numerator = getNumerator(denominator)
    return abs(decimal.Decimal(numerator) / denominator - pi)


def getPiContinuedFraction(size):  # also https://oeis.org/A001203
    f = []
    p = pi - 3
    for _ in range(size):
        p = 1 / p
        f.append(int(p))
        p -= int(p)
    return f


def getDistancesToTheNextMinimum(piContinuedFractionSize):
    distances = [1]
    for item in getPiContinuedFraction(piContinuedFractionSize):
        if len(distances) == 1:
            prev = 1
        else:
            prev = distances[-2]
        for _ in range(item):
            distances.append(distances[-1] + prev)
    return distances


def getBestApproximation(min, max):
    cur = min
    minDist = getDistanceToPi(cur)
    steps = getDistancesToTheNextMinimum(27)
    while True:
        for step in steps:
            if cur + step > max:
                return str(getNumerator(cur)) + "/" + str(cur)
            dist = getDistanceToPi(cur + step)
            if dist < minDist:
                minDist = dist
                cur += step
                break


min, max = map(int, input().split())
print(getBestApproximation(min, max))