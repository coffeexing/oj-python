t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    cnt = 0
    flag = False
    for i in a:
        if i == 0:
            flag = True
            if flag:
                cnt += 1
        else:
            result = max(result, cnt)
            cnt = 0
            flag = False

    print(max(result, cnt))