x = list(map(int, input().split()))
abc = max(x)

for i in range(0, 4):
    if x[i] != abc:
        print(abc - x[i], end=' ')