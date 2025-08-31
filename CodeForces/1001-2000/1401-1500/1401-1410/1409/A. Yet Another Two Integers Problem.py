t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    diff = abs(a - b)
    if diff % 10 == 0:
        print(diff // 10)
    else:
        print(diff // 10 + 1)