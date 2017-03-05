# What is the largest prime factor of a given number


    def is_prime(n):
        if n % 2 == 0:
            return False
        for i in range(3, int(n/2)+1, 2):
            if i > 5 and i % 5 == 0:
                return False
            if n % i == 0:
                return False
        return True


    def prime_factors(n):
        if is_prime(n):
            return n
        l = []
        for i in range(3, int(n/2)+1, 2):
            if n % i == 0 and is_prime(i):
                l.append(i)
        return l[-1]


    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(prime_factors(n))

