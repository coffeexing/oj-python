import math

n = int(input())

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in range(4, math.ceil(n / 2) + 1):
    if not (is_prime(i) or is_prime(n - i)):
        print(i, n - i)
        exit(0)