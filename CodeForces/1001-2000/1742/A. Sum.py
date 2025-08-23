t = int(input())

for _ in range(t):
    x = list(map(int, input().split()))
    x.sort()
    a, b, c = x[0], x[1], x[2]
    if a + b == c:
        print("YES")
    else:
        print("NO")