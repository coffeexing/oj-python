t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i - 1]

    for _ in range(q):
        l, r, k = map(int, input().split())
        res = k * (r - l + 1) + s[n] - (s[r] - s[l - 1])
        if res % 2 == 1:
            print("YES")
        else:
            print("NO")