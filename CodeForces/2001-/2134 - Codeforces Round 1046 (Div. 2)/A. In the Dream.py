t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    x = max(a, b)
    y = min(a, b)
    if x > 2 * (y + 1):
        print('NO')
        continue

    x = max(c - a, d - b)
    y = min(c - a, d - b)

    if x > 2 * (y + 1):
        print('NO')
        continue

    print('YES')
