n = int(input())
s = list(map(int, input().split()))
max_s = s[0]
min_s = s[0]

cnt = 0
for i in range(1, n):
    if s[i] > max_s:
        cnt += 1
        max_s = s[i]
    elif s[i] < min_s:
        cnt += 1
        min_s = s[i]

print(cnt)