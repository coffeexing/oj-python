n = int(input())
s = str(input())
cnt = 0
pivot = s[0]

for i in range(1, n):
    ch = s[i]
    if ch == pivot:
        cnt += 1
    else:
        pivot = ch

print(cnt)