l = [0, 1]

def fibonacci(n):
    if n < len(l):
        return l[n]
    
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(40):
    print(i, '-->', fibonacci(i))
# n = int(input())
# print(fibonacci(n))
