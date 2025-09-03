import math

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    s_min = ((1 + k) * k) // 2
    s_max = (((n - k + 1) + n) * k) // 2
    if s_min <= x <= s_max:
        print("YES")
    else:
        print("NO")
