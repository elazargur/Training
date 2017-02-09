T = int(input())

def split_string(s):
    even = [c for i, c in enumerate(s) if i % 2 == 0]
    odd = [c for i, c in enumerate(s) if i % 2 != 0]
    print('{} {}'.format(''.join(even), ''.join(odd)))


for case in range(T):
    split_string(input())
