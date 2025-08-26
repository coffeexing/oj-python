t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = sum([x % 2 == 1 for x in a])
    if cnt % 2 == 0:
        print('YES')
    else:
        print('NO')