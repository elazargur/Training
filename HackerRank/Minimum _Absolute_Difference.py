

# def pairs(l):
#     minimum = abs(l[0] - l[1])
#     for i in range(1, len(l)):
#         if abs(l[0] - l[i]) < minimum:
#             minimum = abs(l[0] - l[i])
#             if minimum == 0:
#                 return 0
#     return minimum
#
#
# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# # your code goes here
#
# minimum = abs(a[0] - a[1])
# for i in range(n - 1):
#     lmin = pairs(a[i:])
#     if lmin == 0:
#         minimum == lmin
#         break
#     if lmin < minimum:
#         minimum = lmin
#
# print(minimum)

l = [1, 5, 2, -10, -9, 3]