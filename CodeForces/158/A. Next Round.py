n, k = map(int, input().split())
s = [int(x) for x in input().split()]
pivot = s[k - 1]
cnt = 0

for i in s:
    if i >= pivot and i > 0:
        cnt += 1
    else:
        break

print(cnt)