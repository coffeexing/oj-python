import math

Y, W = map(int, input().split())
D = max(Y, W)
N = math.gcd(6 - D + 1, 6)
A = (6 - D + 1) // N
B = 6 // N
print(f'{A}/{B}')