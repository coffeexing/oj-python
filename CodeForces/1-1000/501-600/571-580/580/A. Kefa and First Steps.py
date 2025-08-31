n = int(input())
a = list(map(int, input().split()))
result = 0
cnt = 1
num = int(1e10)

for i in a:
    if i < num:
        result = max(result, cnt)
        cnt = 1
    else:
        cnt += 1
    num = i

print(max(result, cnt))