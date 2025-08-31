t = int(input())

for _ in range(t):
    s = list(map(int, input().split()))
    if sum(s) - min(s) >= 10:
        print('YES')
    else:
        print('NO')