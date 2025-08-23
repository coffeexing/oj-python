n, k = map(int, input().split())

t = 240 - k
curr = 0
cnt = 0
for i in range(1, n + 1):
    if curr + i * 5 <= t:
        curr += i * 5
        cnt += 1
    else:
        break

print(cnt)