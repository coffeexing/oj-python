n, m = map(int, input().split())
day = n
while n >= m:
    k = n // m
    n %= m
    n += k
    day += k
print(day)