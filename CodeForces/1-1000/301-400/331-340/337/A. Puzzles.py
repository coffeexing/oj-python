n, m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
minus = 1000

for i in range(m - n + 1):
    minus = min(minus, f[i + n - 1] - f[i])

print(minus)