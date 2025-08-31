a = list(map(int, input().split()))
s = [int(ch) for ch in input()]
c = 0
for i in s:
    c += a[i - 1]
print(c)