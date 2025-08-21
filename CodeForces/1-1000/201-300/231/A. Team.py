n = int(input())
cnt = 0

for i in range(n):
    s = [int(x) for x in input().split()]
    if sum(s) >= 2:
        cnt += 1

print(cnt)