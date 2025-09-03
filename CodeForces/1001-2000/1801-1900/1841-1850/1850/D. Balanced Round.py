t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    result = 1
    cnt = 1
    for i in range(1, n):
        if a[i] - a[i - 1] <= k:
            cnt += 1
        else:
            result = max(result, cnt)
            cnt = 1
    print(n - max(result, cnt))
