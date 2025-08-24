n = int(input())
a = list(map(int, input().split()))

sereja = 0
dima = 0

for i in range(n):
    curr = max(a[0], a[-1])
    index = a.index(curr)
    a.pop(index)
    if i % 2 == 0:
        sereja += curr
    else:
        dima += curr

print(sereja, dima)