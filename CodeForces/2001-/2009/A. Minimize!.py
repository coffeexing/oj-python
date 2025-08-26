t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    val = int(1e10)
    for c in range(a, b + 1):
        val = min(val, (c - a) + (b - c))
    print(val)