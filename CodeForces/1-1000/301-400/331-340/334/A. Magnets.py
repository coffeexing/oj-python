n = int(input())
pre = input()
cnt = 1

for i in range(1, n):
    curr = input()
    if pre != curr:
        cnt += 1
    pre = curr

print(cnt)