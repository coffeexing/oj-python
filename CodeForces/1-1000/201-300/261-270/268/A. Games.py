n = int(input())
h = [0] * n
a = [0] * n
for i in range(n):
    h[i], a[i] = map(int, input().split())

cnt = 0
for i in range(n):
    for j in range(n):
        if i != j and h[i] == a[j]:
            cnt += 1

print(cnt)