from string import digits, ascii_lowercase

def lowercase_dict():
    d = {}
    for letter in ascii_lowercase:
        d[letter] = 0
    return d

# local
# for test in range(T):
#     N = int(input())
#     s = int(input())
#     numbers = [int(arr_temp) for arr_temp in input().strip().split(' ')]