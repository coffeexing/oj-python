n = int(input())
t = list(map(int, input().split()))

a, b, c = [], [], []
for i in range(n):
    if t[i] == 1:
        a.append(i + 1)
    elif t[i] == 2:
        b.append(i + 1)
    elif t[i] == 3:
        c.append(i + 1)

w = min(len(a), len(b), len(c))
print(w)
for i in range(w):
    print(a[i], b[i], c[i])