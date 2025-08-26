n, k = map(int, input().split())
y = list(map(int, input().split()))

cnt = [x <= 5 - k for x in y]
print(sum(cnt) // 3)