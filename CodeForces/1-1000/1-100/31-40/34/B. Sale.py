n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
earn = 0
for i in range(n):
    if i < m and a[i] <= 0:
        earn += -a[i]
print(earn)
